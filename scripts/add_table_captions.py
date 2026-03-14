with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# We need to add \captionof{table}{...} after each significant table's \end{longtable} or \end{tabular}
# Strategy: find specific markers near each table and add caption

# =============== TABLE 1: KHUNG NHẬN DẠNG (L187-216) ===============
old = "\\end{longtable}\n}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 1:"
new = "\\end{longtable}\n}\n\\captionof{table}{Khung nhận dạng đề thi nhanh -- Quick Exam Pattern Recognition}\\label{tab:khung-nhan-dang}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 1:"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 1 - Khung nhận dạng")
else:
    print("MISS: Table 1")

# =============== TABLE 2: Space Complexity (L328-360) ===============
old = "\\end{longtable}\n}\n\n\\whyprompt{Tại sao Merge Sort cần"
new = "\\end{longtable}\n}\n\\captionof{table}{So sánh Space Complexity chi tiết các thuật toán sắp xếp}\\label{tab:space-complexity}\n\n\\whyprompt{Tại sao Merge Sort cần"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 2 - Space Complexity")
else:
    print("MISS: Table 2")

# =============== TABLE 3: Bảng tổng hợp sorting (L485-523) ===============
old = "\\end{longtable}\n}\n\n\\subsection{2.2 Bubble Sort}"
new = "\\end{longtable}\n}\n\\captionof{table}{Bảng tổng hợp Complexity các thuật toán sắp xếp}\\label{tab:sorting-summary}\n\n\\subsection{2.2 Bubble Sort}"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 3 - Sorting summary")
else:
    print("MISS: Table 3")

# =============== TABLE 4: Insertion Sort trace (inside traceyourself) ===============
# Skip - this is an exercise fill-in table, not a data table

# =============== TABLE 5: Master Theorem 3 cases (L1205-1228) ===============
old = "\\end{longtable}\n}\n\n\\textbf{Lưu ý:"
new = "\\end{longtable}\n}\n\\captionof{table}{Master Theorem -- Ba trường hợp}\\label{tab:master-theorem}\n\n\\textbf{Lưu ý:"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 4 - Master Theorem")
else:
    print("MISS: Table 4")

# =============== TABLE 5: Master Theorem examples (L1234-1272) ===============
old = "\\end{longtable}\n}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 4:"
new = "\\end{longtable}\n}\n\\captionof{table}{Ví dụ áp dụng Master Theorem}\\label{tab:master-examples}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 4:"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 5 - Master Theorem examples")
else:
    print("MISS: Table 5")

# =============== TABLE 6: Adjacency Matrix (graph) ===============
# L1543 - adjacency matrix example - skip (illustration, not data table)

# =============== TABLE 7: Kruskal trace (L1560-1586) ===============
old = "\\end{tabular}\n\\end{center}\n\\captionof{figure}{Kruskal"
new = "\\end{tabular}\n\\captionof{table}{Kruskal -- Trace từng bước trên đồ thị mẫu}\\label{tab:kruskal-trace}\n\\end{center}\n\\captionof{figure}{Kruskal"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 6 - Kruskal trace")
else:
    print("MISS: Table 6 - Kruskal trace")

# =============== TABLE 7: Prim trace ===============
# Find Prim trace table
old = "\\end{tabular}\n\\end{center}\n\\captionof{figure}{Prim"
new = "\\end{tabular}\n\\captionof{table}{Prim -- Trace từng bước trên đồ thị mẫu}\\label{tab:prim-trace}\n\\end{center}\n\\captionof{figure}{Prim"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 7 - Prim trace")
else:
    print("MISS: Table 7 - Prim trace")

# =============== TABLE 8: Kruskal vs Prim comparison (L1734) ===============
old = "\\end{tabular}\n\\end{center}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 6:"
new = "\\end{tabular}\n\\captionof{table}{So sánh Kruskal và Prim}\\label{tab:kruskal-vs-prim}\n\\end{center}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 6:"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 8 - Kruskal vs Prim")
else:
    print("MISS: Table 8")

# =============== TABLE 9: Dijkstra trace ===============
# Find the Dijkstra trace table near the edge list
old = "\\end{tabular}\n\\end{center}\n\n\\textbf{Bảng trace Dijkstra"
new = "\\end{tabular}\n\\captionof{table}{Dijkstra -- Danh sách cạnh đồ thị mẫu}\\label{tab:dijkstra-edges}\n\\end{center}\n\n\\textbf{Bảng trace Dijkstra"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 9 - Dijkstra edges")
else:
    print("MISS: Table 9")

# =============== TABLE 10: Dijkstra trace table ===============
old = "\\end{tabular}\n\\end{center}\n\n\\textbf{Đường đi ngắn nhất"
new = "\\end{tabular}\n\\captionof{table}{Dijkstra -- Bảng trace khoảng cách từng bước}\\label{tab:dijkstra-trace}\n\\end{center}\n\n\\textbf{Đường đi ngắn nhất"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 10 - Dijkstra trace")
else:
    print("MISS: Table 10")

# =============== TABLE 11: Floyd-Warshall trace ===============
# Multiple Floyd tables - find the initial D^0 table
old = "\\end{tabular}\n\\end{center}\n\n\\textbf{Bước $k=1$"
new = "\\end{tabular}\n\\captionof{table}{Floyd-Warshall -- Ma trận khoảng cách ban đầu $D^{(0)}$}\\label{tab:floyd-d0}\n\\end{center}\n\n\\textbf{Bước $k=1$"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 11 - Floyd D0")
else:
    print("MISS: Table 11")

# =============== TABLE 12: DP vs D&C comparison ===============
old = "\\end{longtable}\n}\n\n\\subsection{\\texorpdfstring{Bài toán Matrix Chain"
new = "\\end{longtable}\n}\n\\captionof{table}{So sánh Dynamic Programming và Divide \\& Conquer}\\label{tab:dp-vs-dc}\n\n\\subsection{\\texorpdfstring{Bài toán Matrix Chain"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 12 - DP vs D&C")
else:
    print("MISS: Table 12")

# =============== TABLE 13: NP reduction ===============
# Find the NP reduction table
old = "\\end{tabular}\n\\end{center}\n\n\\feynman{Giải thích P vs NP"
new = "\\end{tabular}\n\\captionof{table}{Ý nghĩa chiều Reduction trong chứng minh NP-Complete}\\label{tab:np-reduction}\n\\end{center}\n\n\\feynman{Giải thích P vs NP"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 13 - NP reduction")
else:
    print("MISS: Table 13")

# =============== TABLE 14: Cheat Sheet Complexity ===============
old = "\\end{longtable}\n}\n\n\\subsection{Công thức cốt lõi}"
new = "\\end{longtable}\n}\n\\captionof{table}{Cheat Sheet -- Bảng tổng hợp Complexity tất cả thuật toán}\\label{tab:cheat-complexity}\n\n\\subsection{Công thức cốt lõi}"
if old in content:
    content = content.replace(old, new, 1)
    print("OK: Table 14 - Cheat Sheet Complexity")
else:
    print("MISS: Table 14")

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("\nDone!")
