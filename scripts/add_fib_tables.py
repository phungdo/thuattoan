with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

tables = {
    'Pseudocode 1: Fibonacci': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Fibonacci Đệ quy}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{if n <= 1: return n} & $\Theta(1)$ & base case \\
\hline
\texttt{return Fib(n-1) + Fib(n-2)} & $T(n-1)+T(n-2)$ & 2 nhánh đệ quy \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Recurrence:} $T(n) = T(n-1) + T(n-2) + \Theta(1)$.\\
\textbf{Time:} Cây đệ quy có $\sim 2^n$ nút (thực tế $\Theta(\varphi^n)$ với $\varphi\approx1.618$) $\to$ \textbf{exponential}.\\
\textbf{Space:} Chiều sâu cây = $n$ $\to$ stack đệ quy $O(n)$.
\end{tcolorbox}
""",

    'Pseudocode 2: Fibonacci': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Fibonacci DP Bottom-up}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{F[0]=0, F[1]=1} & $2$ & $\Theta(1)$ khởi tạo \\
\hline
\texttt{for i = 2 to n} & $n-1$ & 1 vòng lặp \\
\hline
\quad \texttt{F[i] = F[i-1] + F[i-2]} & $n-1$ & $\Theta(1)$ mỗi lần \\
\hline
\texttt{return F[n]} & $1$ & $\Theta(1)$ \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} 1 vòng \texttt{for} chạy $n-1$ lần $\to$ $\Theta(n)$. \textit{Nhanh gấp cấp số mũ so với đệ quy!}\\
\textbf{Space:} Mảng $F[0..n]$ có $n+1$ phần tử $\to$ $\Theta(n)$.
\end{tcolorbox}
""",

    'Pseudocode 3: Fibonacci': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Fibonacci DP tối ưu space}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{a := 0, b := 1} & $2$ & $\Theta(1)$ khởi tạo \\
\hline
\texttt{for i = 2 to n} & $n-1$ & 1 vòng lặp \\
\hline
\quad \texttt{c:=a+b; a:=b; b:=c} & $n-1$ & $\Theta(1)$ mỗi lần \\
\hline
\texttt{return c} & $1$ & $\Theta(1)$ \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} Giống cách 2: 1 vòng \texttt{for} $\to$ $\Theta(n)$.\\
\textbf{Space:} Chỉ dùng 3 biến $a, b, c$ $\to$ $O(1)$! \textit{Tối ưu hơn cách 2 (từ $\Theta(n)$ xuống $O(1)$).}
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
