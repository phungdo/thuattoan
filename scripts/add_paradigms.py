with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

# ========== 1. DIVIDE & CONQUER (Ch.3) ==========
# Insert after pitfall line (L1150) and before \subsection{Ba phương pháp} (L1152)
dc_idea = r"""
\subsection{Ý tưởng Chia để trị (Divide \& Conquer)}\label{y-tuong-dc}

Divide \& Conquer là mô hình thiết kế thuật toán gồm \textbf{3 bước}:

\begin{enumerate}
\item \textbf{Divide (Chia):} Chia bài toán kích thước $n$ thành $a$ bài toán con kích thước $n/b$.
\item \textbf{Conquer (Trị):} Giải đệ quy từng bài toán con. Nếu bài toán con đủ nhỏ, giải trực tiếp (base case).
\item \textbf{Combine (Kết hợp):} Gộp nghiệm các bài toán con thành nghiệm bài toán gốc.
\end{enumerate}

\textbf{Công thức đệ quy tổng quát:}
\[T(n) = aT(n/b) + f(n)\]
trong đó $a$ = số bài toán con, $n/b$ = kích thước mỗi bài con, $f(n)$ = chi phí chia + gộp.

\textbf{Ví dụ điển hình:}
\begin{itemize}
\item \textbf{Merge Sort:} $a=2, b=2, f(n)=\Theta(n)$ (chia giữa, merge $\Theta(n)$) $\to T(n)=\Theta(n\lg n)$.
\item \textbf{Quick Sort:} $a=2, b$ phụ thuộc pivot, $f(n)=\Theta(n)$ (Partition).
\item \textbf{Binary Search:} $a=1, b=2, f(n)=\Theta(1)$ $\to T(n)=\Theta(\lg n)$.
\end{itemize}

"""

# Find insertion point: after L1150 (pitfall), before L1152 (\subsection{Ba phương pháp})
insert_idx = 1151  # 0-indexed line 1151 = after pitfall blank line
lines.insert(insert_idx, dc_idea)
print("Inserted D&C Ý tưởng at line 1152")

# ========== 2. GREEDY (Ch.5) ==========
# Insert after pitfall (L1400 original, now shifted) before \subsection{5.1}
# Need to recalculate: original L1401 + 1 (dc_idea is 1 insert) 
greedy_idea = r"""
\subsection{Ý tưởng thuật toán Tham lam (Greedy)}\label{y-tuong-greedy}

Thuật toán Tham lam xây dựng nghiệm từng bước, mỗi bước chọn phương án \textbf{tốt nhất tại thời điểm đó} (locally optimal) mà không quay lui. Khác với DP (xét mọi khả năng), Greedy chỉ xét \textbf{1 lựa chọn duy nhất} mỗi bước.

\textbf{Khi nào Greedy cho nghiệm tối ưu?} Khi bài toán thỏa mãn 2 tính chất:
\begin{enumerate}
\item \textbf{Greedy-choice property:} Tồn tại nghiệm tối ưu toàn cục chứa lựa chọn tham lam (chọn cục bộ tốt nhất không loại trừ nghiệm tối ưu).
\item \textbf{Optimal substructure:} Sau khi chọn greedy, bài toán con còn lại cũng có nghiệm tối ưu.
\end{enumerate}

\textbf{So sánh với DP:} Greedy quyết định \textit{trước khi} giải bài toán con (top-down, không quay lui). DP quyết định \textit{sau khi} giải hết bài toán con (bottom-up hoặc memoized). Greedy nhanh hơn ($O(n \lg n)$ vs $O(n^2)$ hoặc $O(n^3)$) nhưng chỉ đúng khi có 2 tính chất trên.

"""

# Find "\subsection{5.1 Phương pháp Greedy" in the shifted content
greedy_target = "\\subsection{5.1 Phương pháp Greedy"
for i, line in enumerate(lines):
    if greedy_target in line:
        lines.insert(i, greedy_idea)
        print(f"Inserted Greedy Ý tưởng at line {i+1}")
        break

# ========== 3. DYNAMIC PROGRAMMING (Ch.7) ==========
dp_idea = r"""
\subsection{Ý tưởng Quy hoạch Động (Dynamic Programming)}\label{y-tuong-dp}

Quy hoạch Động (DP) giải bài toán tối ưu bằng cách \textbf{chia thành bài toán con chồng lấp} (overlapping subproblems), giải mỗi bài con \textbf{đúng 1 lần}, lưu kết quả vào bảng để tái sử dụng.

\textbf{Khi nào dùng DP?} Khi bài toán có 2 tính chất:
\begin{enumerate}
\item \textbf{Optimal substructure:} Nghiệm tối ưu bài toán lớn \textit{chứa} nghiệm tối ưu bài toán con.
\item \textbf{Overlapping subproblems:} Các bài toán con được gọi lại nhiều lần (đệ quy ngây thơ sẽ tính lại $\to$ lãng phí).
\end{enumerate}

\textbf{Hai phương pháp triển khai:}
\begin{itemize}
\item \textbf{Top-down (Memoization):} Viết đệ quy + cache. Dễ code nhưng overhead gọi hàm.
\item \textbf{Bottom-up (Tabulation):} Điền bảng từ bài toán nhỏ $\to$ lớn. Hiệu quả hơn, không cần stack đệ quy.
\end{itemize}

\textbf{So sánh D\&C vs DP:} D\&C chia thành bài toán con \textit{không chồng lấp} (independent), DP chia thành bài toán con \textit{chồng lấp} (shared). Nếu có overlapping mà dùng D\&C thẳng $\to$ exponential time (vd: Fibonacci naive $O(2^n)$).

"""

# Find "\subsection{\texorpdfstring{Bốn bước thiết kế DP"
dp_target = "Bốn bước thiết kế DP"
for i, line in enumerate(lines):
    if dp_target in line:
        lines.insert(i, dp_idea)
        print(f"Inserted DP Ý tưởng at line {i+1}")
        break

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print("\nDone!")
