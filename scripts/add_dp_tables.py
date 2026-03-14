with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

tables = {
    'Pseudocode 17: Pascal': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Pascal Triangle DP ($O(nk)$ space)}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{C[0..n][0..k]} khởi tạo & $(n+1)(k+1)$ & cấp phát bảng 2D \\
\hline
\texttt{for i = 0 to n} & $n+1$ & vòng ngoài \\
\hline
\quad \texttt{for j = 0 to min(i,k)} & $\sum_{i=0}^{n}\min(i,k)+1$ & vòng trong \\
\hline
\quad\quad \texttt{C[i][j] = C[i-1][j] + C[i-1][j-1]} & $\leq nk$ & $\Theta(1)$ mỗi ô \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} 2 vòng lồng: $i$ chạy $n+1$ lần, $j$ chạy tối đa $\min(i,k)$ $\to$ tổng $\leq n \cdot k$ ô $\to$ $O(nk)$.\\
\textbf{Space:} Bảng 2D $C[0..n][0..k]$ có $(n+1)(k+1)$ ô $\to$ $O(nk)$.
\end{tcolorbox}
""",

    'Pseudocode 18: Pascal': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Pascal Triangle DP tối ưu ($O(k)$ space)}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{C[0..k], C[0] = 1} & $k+1$ & cấp phát mảng 1D \\
\hline
\texttt{for i = 1 to n} & $n$ & vòng ngoài \\
\hline
\quad \texttt{for j = min(i,k) downto 1} & $\leq nk$ & \textbf{duyệt ngược} (quan trọng!) \\
\hline
\quad\quad \texttt{C[j] = C[j] + C[j-1]} & $\leq nk$ & $\Theta(1)$ mỗi lần \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} Vẫn $O(nk)$ -- cùng số phép tính như cách 1.\\
\textbf{Space:} Chỉ dùng 1 mảng $C[0..k]$ $\to$ $O(k)$! \textit{Tối ưu từ $O(nk)$ xuống $O(k)$ nhờ duyệt \textbf{ngược} $j$.}\\
{\small (Duyệt ngược đảm bảo $C[j-1]$ chưa bị ghi đè khi tính $C[j]$ -- giống kỹ thuật 0/1 Knapsack.)}
\end{tcolorbox}
""",

    'Pseudocode 19: Floyd': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Floyd-Warshall}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{D = W} (copy ma trận) & $n^2$ & $\Theta(n^2)$ \\
\hline
\texttt{for k = 1 to n} & $n$ & vòng ngoài (đỉnh trung gian) \\
\hline
\quad \texttt{for i = 1 to n} & $n^2$ & vòng giữa \\
\hline
\quad\quad \texttt{for j = 1 to n} & $n^3$ & vòng trong \\
\hline
\quad\quad\quad \texttt{D[i][j] = min(...)} & $n^3$ & $\Theta(1)$ mỗi lần \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} 3 vòng \texttt{for} lồng nhau, mỗi vòng $n$ lần $\to$ $n \times n \times n = \Theta(n^3)$.\\
\textbf{Space:} Ma trận $D[n \times n]$ $\to$ $\Theta(n^2)$. {\small (Có thể cập nhật in-place trên 1 ma trận vì $D^{(k)}[i][k] = D^{(k-1)}[i][k]$.)}
\end{tcolorbox}
""",
}

inserted = 0
for target, table in reversed(list(tables.items())):
    for i, line in enumerate(lines):
        if target in line:
            for j in range(i, min(i+20, len(lines))):
                if '\\end{tcolorbox}' in lines[j]:
                    lines.insert(j+1, table)
                    inserted += 1
                    print(f"OK: {target} at L{j+2}")
                    break
            break

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print(f"\nDone! Inserted {inserted} complexity tables")
