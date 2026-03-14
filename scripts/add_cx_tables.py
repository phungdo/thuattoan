with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

# Complexity tables to insert after each sorting pseudocode's \end{tcolorbox}
tables = {
    'Pseudocode 3a: Bubble': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Bubble Sort}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{for i = 1 to n-1} & $n-1$ & vòng ngoài \\
\hline
\quad \texttt{for j = 1 to n-i} & $\sum_{i=1}^{n-1}(n-i)=\frac{n(n-1)}{2}$ & vòng trong \\
\hline
\quad\quad \texttt{if A[j]>A[j+1]: swap} & $\frac{n(n-1)}{2}$ & $\Theta(1)$ mỗi lần \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} $T(n)=\frac{n(n-1)}{2}=\Theta(n^2)$ (worst/avg). Best $\Theta(n)$ nếu thêm cờ early stop.\\
\textbf{Space:} $O(1)$ -- chỉ dùng biến $i, j$, swap tại chỗ (in-place).
\end{tcolorbox}
""",

    'Pseudocode 3b: Selection': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Selection Sort}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{for i = 1 to n-1} & $n-1$ & vòng ngoài \\
\hline
\quad \texttt{min\_idx = i} & $n-1$ & $\Theta(1)$ \\
\hline
\quad \texttt{for j = i+1 to n} & $\sum_{i=1}^{n-1}(n-i)=\frac{n(n-1)}{2}$ & tìm min \\
\hline
\quad \texttt{swap(A[i], A[min\_idx])} & $n-1$ & $\Theta(1)$ \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} $T(n)=\frac{n(n-1)}{2}=\Theta(n^2)$ mọi trường hợp (luôn duyệt hết).\\
\textbf{Space:} $O(1)$ -- chỉ dùng biến $i, j, \text{min\_idx}$ (in-place).
\end{tcolorbox}
""",

    'Pseudocode 4: Insertion': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Insertion Sort (CLRS \S 2.2)}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{for j = 2 to n} & $n-1$ & vòng ngoài \\
\hline
\quad \texttt{key = A[j]} & $n-1$ & $\Theta(1)$ \\
\hline
\quad \texttt{i = j - 1} & $n-1$ & $\Theta(1)$ \\
\hline
\quad \texttt{while i>0 and A[i]>key} & $\sum t_j$ & $t_j$ = số dịch ở bước $j$ \\
\hline
\quad\quad \texttt{A[i+1] = A[i]; i--} & $\sum (t_j-1)$ & $\Theta(1)$ mỗi lần \\
\hline
\quad \texttt{A[i+1] = key} & $n-1$ & $\Theta(1)$ \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time Best} (đã sắp): $t_j=1$ $\forall j$ $\to$ while không chạy $\to$ $T(n)=\Theta(n)$.\\
\textbf{Time Worst} (sắp ngược): $t_j=j$ $\to$ $\sum_{j=2}^{n}j=\frac{n(n-1)}{2}$ $\to$ $T(n)=\Theta(n^2)$.\\
\textbf{Space:} $O(1)$ -- chỉ dùng biến $key, i, j$ (in-place).
\end{tcolorbox}
""",

    'Pseudocode 5: Merge': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Merge Sort}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Bước D\&C} & \textbf{Chi phí} & \textbf{Giải thích} \\
\hline
\textbf{Divide:} tính $q=\lfloor(p+r)/2\rfloor$ & $\Theta(1)$ & 1 phép chia \\
\hline
\textbf{Conquer:} gọi đệ quy 2 nửa & $2T(n/2)$ & 2 bài con, mỗi bài $n/2$ \\
\hline
\textbf{Combine:} Merge 2 mảng con & $\Theta(n)$ & duyệt tuyến tính $n$ phần tử \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Recurrence:} $T(n) = 2T(n/2) + \Theta(n)$.\\
\textbf{Giải} (Master Theorem Case 2, $a=2, b=2, f(n)=\Theta(n)=\Theta(n^{\log_2 2})$): $T(n)=\Theta(n\lg n)$.\\
\textbf{Space:} Merge tạo mảng tạm $L, R$ tổng $\Theta(n)$ + stack đệ quy $O(\lg n)$ $\to$ $\Theta(n)$.
\end{tcolorbox}
""",

    'Pseudocode 6: Quick': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Quick Sort}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Bước} & \textbf{Chi phí} & \textbf{Giải thích} \\
\hline
\textbf{Partition:} duyệt $n-1$ phần tử & $\Theta(n)$ & 1 vòng for \\
\hline
\textbf{Đệ quy 2 nửa} & $T(k) + T(n-k-1)$ & $k$ = vị trí pivot \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Best case} (pivot chia đều): $T(n)=2T(n/2)+\Theta(n)$ $\to$ $\Theta(n\lg n)$.\\
\textbf{Worst case} (pivot lệch cực): $T(n)=T(n-1)+\Theta(n)$ $\to$ $\Theta(n^2)$.\\
\textbf{Average case:} Mọi cách chia trung bình cho $\Theta(n\lg n)$.\\
\textbf{Space:} Stack đệ quy sâu $O(\lg n)$ avg, $O(n)$ worst. Không cần mảng phụ (in-place).
\end{tcolorbox}
""",

    'Pseudocode 8: Heap': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Heap Sort}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Thao tác} & \textbf{Chi phí} & \textbf{Giải thích} \\
\hline
\texttt{MaxHeapify(A, i)} & $O(\lg n)$ & đi xuống tối đa $\lg n$ tầng \\
\hline
\texttt{BuildMaxHeap(A)} & $O(n)$ & \textit{không phải} $O(n\lg n)$! \\
\hline
\quad (Lý do: $\sum_{h=0}^{\lg n}\lceil n/2^{h+1}\rceil \cdot O(h) = O(n)$) & & tổng telescoping \\
\hline
\texttt{HeapSort}: vòng for $n-1$ lần & $(n-1)\cdot O(\lg n)$ & swap gốc + MaxHeapify \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} BuildMaxHeap $O(n)$ + HeapSort loop $O(n\lg n)$ $\to$ $\Theta(n\lg n)$ mọi trường hợp.\\
\textbf{Space:} $O(1)$ -- heap lưu ngay trong mảng $A$ (in-place), không cần mảng phụ.
\end{tcolorbox}
""",

    'Pseudocode 9: Counting': r"""
\begin{tcolorbox}[colback=yellow!5, colframe=orange!50, boxrule=0.5pt, arc=2pt, title={\small\textbf{Phân tích Complexity -- Counting Sort}}]
\begin{tabular}{|l|l|l|}
\hline
\textbf{Dòng code} & \textbf{Số lần chạy} & \textbf{Chi phí} \\
\hline
\texttt{let C[0..k] = all zeros} & $k+1$ & khởi tạo mảng đếm \\
\hline
\texttt{for j = 1 to n: C[A[j]]++} & $n$ & đếm tần suất \\
\hline
\texttt{for i = 1 to k: C[i] += C[i-1]} & $k$ & cộng dồn \\
\hline
\texttt{for j = n downto 1: B[C[A[j]]]=A[j]} & $n$ & đặt vào output \\
\hline
\end{tabular}
\vspace{0.2cm}

\textbf{Time:} $\Theta(n+k)$ -- 2 vòng $\Theta(n)$ + 1 vòng $\Theta(k)$. \textit{Tuyến tính} khi $k=O(n)$.\\
\textbf{Space:} Mảng $C[0..k]$: $\Theta(k)$ + mảng output $B[1..n]$: $\Theta(n)$ $\to$ $\Theta(n+k)$. \textit{Không} in-place.
\end{tcolorbox}
""",
}

# Insert tables after each pseudocode's \end{tcolorbox}
inserted = 0
for target, table in reversed(list(tables.items())):
    for i, line in enumerate(lines):
        if target in line:
            # Find the next \end{tcolorbox}
            for j in range(i, min(i+40, len(lines))):
                if '\\end{tcolorbox}' in lines[j]:
                    # Insert table after this line
                    lines.insert(j+1, table)
                    inserted += 1
                    print(f"OK: {target[:30]}... at L{j+2}")
                    break
            break

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print(f"\nDone! Inserted {inserted} complexity tables")
