class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.parent[x] != x: self.parent[x] = self.parent[self.parent[x]]; x = self.parent[x]
        return x
    def issame(self, a, b): return self.find(a) == self.find(b)
    def unite(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]: a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]: self.rank[a] += 1

# Using KRUSKAL video graph (no CF edge)
G_kruskal = {
    'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
    'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
    'C': [(3, 'A', 'C'), (5, 'D', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
    'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
    'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
    'F': [(9, 'G', 'F'), (8, 'E', 'F'), (7, 'D', 'F')],
    'G': [(9, 'F', 'G')],
}

# Collect unique edges
seen = set()
edges = []
for node, adj in G_kruskal.items():
    for (cost, n1, n2) in adj:
        key = tuple(sorted([n1, n2]))
        if key not in seen:
            seen.add(key)
            edges.append((cost, n1, n2))
edges.sort()
print("=== KRUSKAL VIDEO EDGES ===")
for e in edges:
    print(f"  {e[1]}{e[2]} = {e[0]}")

# Using PRIM video graph (has CF edge)
G_prim = {
    'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
    'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
    'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
    'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
    'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
    'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
    'G': [(9, 'F', 'G')],
}
seen2 = set()
edges2 = []
for node, adj in G_prim.items():
    for (cost, n1, n2) in adj:
        key = tuple(sorted([n1, n2]))
        if key not in seen2:
            seen2.add(key)
            edges2.append((cost, n1, n2))
edges2.sort()
print("\n=== PRIM VIDEO EDGES ===")
for e in edges2:
    print(f"  {e[1]}{e[2]} = {e[0]}")
print(f"\nDifference: Prim has CF(6) that Kruskal doesn't")
