import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np
import geopandas as gpd
from shapely.geometry import Point, LineString

BD = "/Users/Apple/Downloads/madrid_barcelona_traffic_prediction_from_air_noise/barcelona"
noise_loc = pd.read_csv(f"{BD}/location_noise_XarxaSoroll_EquipsMonitor_Instal.csv")
raw_trams = pd.read_csv(f"{BD}/transit_relacio_trams.csv")
air_loc = pd.read_csv(f"{BD}/air_location_2025_qualitat_aire_estacions.csv")
noise_data = pd.read_csv(f"{BD}/noise_hourly.csv")
traffic_data = pd.read_csv(f"{BD}/traffic_trams_hourly.csv")

active_sensors = set(noise_data["Id_Instal"].unique())
active_stats = traffic_data.groupby("idTram")["estatActual_mean"].agg(["std","count"])
good_trams = set(active_stats[(active_stats["std"] > 0.1) & (active_stats["count"] > 100)].index)

noise_gdf = gpd.GeoDataFrame(noise_loc,
    geometry=gpd.points_from_xy(noise_loc["Longitud"], noise_loc["Latitud"]), crs="EPSG:4326")
noise_m = noise_gdf.to_crs(25831)

lines = []; ids = []
for _, row in raw_trams.iterrows():
    try:
        c = str(row["Coordenades"]).split(",")
        coords = [(float(c[i]), float(c[i+1])) for i in range(0, len(c), 2)]
        if len(coords) >= 2:
            lines.append(LineString(coords))
            ids.append(row["Tram"])
    except:
        pass
all_traf = gpd.GeoDataFrame({"Tram": ids}, geometry=lines, crs="EPSG:4326").to_crs(25831)
good_traf = all_traf[all_traf["Tram"].isin(good_trams)]

air_unique = air_loc.drop_duplicates("Estacio")
air_pts = gpd.GeoDataFrame(air_unique,
    geometry=gpd.points_from_xy(air_unique["Longitud"], air_unique["Latitud"]), crs="EPSG:4326")
air_m = air_pts.to_crs(25831)

done = {4, 44}
remaining = air_m[~air_m["Estacio"].isin(done)]

air_data = pd.read_csv(f"{BD}/air_quality_hourly.csv")

for _, station in remaining.iterrows():
    est = station["Estacio"]
    name = station["nom_cabina"].replace("Barcelona - ", "")
    district = station["Nom_districte"]
    pols = sorted([p for p in air_data[air_data["Estacio"]==est]["contaminant"].dropna().unique()
                   if not p.startswith("Flow") and "Black" not in p])

    dists_noise = noise_m.geometry.distance(station.geometry)
    nearby_noise = noise_m[dists_noise < 1000].copy()
    nearby_noise["dist_to_air"] = dists_noise[dists_noise < 1000]
    nearby_noise_active = nearby_noise[nearby_noise["Id_Instal"].isin(active_sensors)]

    print(f"\n{'='*80}")
    print(f"Est. {est}: {name} ({district})")
    print(f"Pollutants: {pols}")
    print(f"Noise sensors within 1000m: {len(nearby_noise)} total, {len(nearby_noise_active)} with data")

    if len(nearby_noise_active) == 0:
        print("  NO noise sensors with data within 1000m!")
        continue

    pairs = []
    for _, ns in nearby_noise_active.iterrows():
        ns_pt = ns.geometry
        dists_traf = good_traf.geometry.distance(ns_pt)
        close_traf = good_traf[dists_traf < 50]
        if len(close_traf) > 0:
            best_idx = dists_traf[dists_traf < 50].idxmin()
            best_tram = good_traf.loc[best_idx, "Tram"]
            best_dist = dists_traf[best_idx]
            pairs.append({
                "sensor_id": ns["Id_Instal"],
                "street": ns["Nom_Carrer"],
                "dist_to_air": ns["dist_to_air"],
                "tram_id": best_tram,
                "dist_to_tram": best_dist,
            })

    if len(pairs) == 0:
        print("  NO pairs with road section < 50m!")
        for _, ns in nearby_noise_active.sort_values("dist_to_air").head(3).iterrows():
            ns_pt = ns.geometry
            dists_traf = good_traf.geometry.distance(ns_pt)
            nearest_idx = dists_traf.idxmin()
            print(f"    Sensor {int(ns['Id_Instal'])} ({ns['Nom_Carrer']}): air={ns['dist_to_air']:.0f}m, nearest tram {good_traf.loc[nearest_idx,'Tram']} at {dists_traf.min():.0f}m")
        continue

    df = pd.DataFrame(pairs).sort_values("dist_to_tram")
    print(f"  Viable pairs (noise ON road <50m): {len(df)}")
    for _, r in df.iterrows():
        print(f"    Sensor {int(r['sensor_id']):>5} ({r['street']:<18}) -> Tram {int(r['tram_id']):>4} ({r['dist_to_tram']:>4.0f}m) | Air: {r['dist_to_air']:>5.0f}m")
