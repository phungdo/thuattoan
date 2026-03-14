with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

count = 0

# TABLE: Master Theorem 3 cases (L1231)
old = "\\end{longtable}\n}\n\n\\textbf{Lưu ý"
if old not in content:
    # Try alternate
    old = "\\end{longtable}\n}\n\n\\textbf{L\u01b0u \u00fd"
new_str = "\\end{longtable}\n}\n\\captionof{table}{Master Theorem -- Ba tr\u01b0\u1eddng h\u1ee3p}\\label{tab:master-theorem}\n\n\\textbf{L\u01b0u \u00fd"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: Master Theorem cases")
else:
    print("MISS: Master Theorem cases")

# TABLE: Kruskal vs Prim comparison (near L1762)
old = "\\end{tabular}\n\\end{center}\n\\captionof{figure}{So s\u00e1nh tr\u1ef1c di\u1ec7n Kruskal vs Prim}"
new_str = "\\end{tabular}\n\\captionof{table}{So s\u00e1nh Kruskal v\u00e0 Prim -- \u0110\u1eb7c \u0111i\u1ec3m v\u00e0 \u01afu \u0111i\u1ec3m}\\label{tab:kruskal-vs-prim}\n\\end{center}\n\\captionof{figure}{So s\u00e1nh tr\u1ef1c di\u1ec7n Kruskal vs Prim}"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: Kruskal vs Prim")
else:
    print("MISS: Kruskal vs Prim")

# TABLE: Dijkstra edge list (L1783)
old = "\\end{tabular}\n\\end{center}\n\n\\textbf{B\u1ea3ng trace Dijkstra"
new_str = "\\end{tabular}\n\\captionof{table}{Dijkstra -- Danh s\u00e1ch c\u1ea1nh \u0111\u1ed3 th\u1ecb m\u1eabu}\\label{tab:dijkstra-edges}\n\\end{center}\n\n\\textbf{B\u1ea3ng trace Dijkstra"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: Dijkstra edges")
else:
    print("MISS: Dijkstra edges")

# TABLE: Dijkstra trace (L1938 area)
old = "\\end{tabular}\n\\end{center}\n\n\\textbf{\u0110\u01b0\u1eddng \u0111i ng\u1eafn nh\u1ea5t"
new_str = "\\end{tabular}\n\\captionof{table}{Dijkstra -- B\u1ea3ng trace kho\u1ea3ng c\u00e1ch t\u1eebng b\u01b0\u1edbc}\\label{tab:dijkstra-trace}\n\\end{center}\n\n\\textbf{\u0110\u01b0\u1eddng \u0111i ng\u1eafn nh\u1ea5t"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: Dijkstra trace")
else:
    print("MISS: Dijkstra trace")

# TABLE: Floyd-Warshall D^0 (L2013 area)
old = "\\end{tabular}\n\\end{center}\n\n\\textbf{B\u01b0\u1edbc $k=1$"
new_str = "\\end{tabular}\n\\captionof{table}{Floyd-Warshall -- Ma tr\u1eadn kho\u1ea3ng c\u00e1ch ban \u0111\u1ea7u $D^{(0)}$}\\label{tab:floyd-d0}\n\\end{center}\n\n\\textbf{B\u01b0\u1edbc $k=1$"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: Floyd D0")
else:
    print("MISS: Floyd D0")

# TABLE: DP vs D&C (L2122)
old = "\\end{longtable}\n}\n\n\\subsection{\\texorpdfstring{B\u00e0i to\u00e1n Matrix Chain"
new_str = "\\end{longtable}\n}\n\\captionof{table}{So s\u00e1nh Dynamic Programming v\u00e0 Divide \\& Conquer}\\label{tab:dp-vs-dc}\n\n\\subsection{\\texorpdfstring{B\u00e0i to\u00e1n Matrix Chain"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: DP vs D&C")
else:
    print("MISS: DP vs D&C")

# TABLE: NP reduction (L2338 area)
old = "\\end{tabular}\n\\end{center}\n\n\\feynman{Gi\u1ea3i th\u00edch P vs NP"
new_str = "\\end{tabular}\n\\captionof{table}{\u00dd ngh\u0129a chi\u1ec1u Reduction trong ch\u1ee9ng minh NP-Complete}\\label{tab:np-reduction}\n\\end{center}\n\n\\feynman{Gi\u1ea3i th\u00edch P vs NP"
if old in content:
    content = content.replace(old, new_str, 1)
    count += 1
    print("OK: NP reduction")
else:
    print("MISS: NP reduction")

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print(f"\nDone! Fixed {count} more tables")
