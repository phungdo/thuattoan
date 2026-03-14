with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

tables = {
    'Pseudocode 12: Greedy': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Greedy Framework (tổng quát)}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Bước} & \textbf{Chi phí} & \textbf{Giải thích} \\
\hline
\texttt{T := empty} & $\Theta(1)$ & khởi tạo \\
\hline
\texttt{Lặp: Chọn a tối ưu cục bộ} & tùy cách chọn & xem thuật toán cụ thể \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} Phụ thuộc bài toán cụ thể. Thường gồm: \textbf{sắp xếp} $O(n\lg n)$ + \textbf{duyệt} $O(n)$ $\to$ $O(n\lg n)$.\\
\textbf{Space:} $O(n)$ cho tập $T$ kết quả. Cấu trúc dữ liệu phụ tùy bài.
\end{tcolorbox}
""",

    'Pseudocode 13: Kruskal': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Kruskal's Algorithm}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{for v in V: MakeSet(v)} & $V$ lần & $O(V)$ \\
\hline
\texttt{Sắp xếp E theo w tăng dần} & 1 lần & $O(E\lg E)$ \\
\hline
\texttt{for (u,v) in E:} & $E$ lần & duyệt tất cả cạnh \\
\hline
\quad \texttt{FindSet(u), FindSet(v)} & $2E$ lần & $O(\alpha(V))$ mỗi lần \\
\hline
\quad \texttt{Union(u,v)} & tối đa $V-1$ & $O(\alpha(V))$ mỗi lần \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} Sắp xếp $O(E\lg E)$ + duyệt $E$ cạnh $\times$ Union-Find $O(\alpha(V))$ $\to$ \textbf{tổng $O(E\lg E) = O(E\lg V)$}.\\
{\small (Vì $E \leq V^2 \Rightarrow \lg E \leq 2\lg V = O(\lg V)$. $\alpha(V)$ gần như hằng số.)}\\
\textbf{Space:} Mảng \texttt{parent[V]} + \texttt{rank[V]} cho Union-Find $\to$ $O(V)$.
\end{tcolorbox}
""",

    'Pseudocode 14: Prim': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Prim's Algorithm}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{for u in V: key[u]=INF} & $V$ & $O(V)$ khởi tạo \\
\hline
\texttt{Q = MinPriorityQueue(V)} & 1 & $O(V)$ build heap \\
\hline
\texttt{u = ExtractMin(Q)} & $V$ lần & $O(\lg V)$ mỗi lần \\
\hline
\texttt{for v in Adj[u]:} & tổng $= 2E$ & mỗi cạnh xét 2 lần \\
\hline
\quad \texttt{DecreaseKey(v)} & tối đa $E$ lần & $O(\lg V)$ mỗi lần \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time} (Min-Heap): $V \cdot O(\lg V)$ ExtractMin + $E \cdot O(\lg V)$ DecreaseKey $\to$ $O((V+E)\lg V) = O(E\lg V)$.\\
{\small (Nếu dùng Fibonacci Heap: DecreaseKey $O(1)$ amortized $\to$ $O(E + V\lg V)$.)}\\
\textbf{Space:} Mảng \texttt{key[V]}, \texttt{$\pi$[V]}, Priority Queue $Q$ chứa $V$ đỉnh $\to$ $O(V)$.
\end{tcolorbox}
""",
}

inserted = 0
for target, table in reversed(list(tables.items())):
    for i, line in enumerate(lines):
        if target in line:
            for j in range(i, min(i+30, len(lines))):
                if '\\end{tcolorbox}' in lines[j]:
                    lines.insert(j+1, table)
                    inserted += 1
                    print(f"OK: {target} at L{j+2}")
                    break
            break

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print(f"\nDone! Inserted {inserted} complexity tables")
