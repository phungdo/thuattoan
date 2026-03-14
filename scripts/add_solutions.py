import re

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

solutions_chapter = r"""
\section{Lời giải -- Tại sao? \& Tự Trace}\label{loi-giai-tai-sao-va-tu-trace}

Phần này cung cấp lời giải chi tiết cho tất cả các hộp \textbf{``? Tại sao?''} và \textbf{``$\triangleright$ Tự Trace''} trong tài liệu, được đánh chỉ mục theo chương.

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}

% ============================================================
\subsection{Chương 1: Nền tảng}

\subsubsection{Tại sao? 1.1 -- Tại sao không dùng đo thời gian thực tế thay cho Big-O?}\label{whyans:1.1}

\textbf{Câu hỏi:} Tại sao ta không dùng đo thời gian chạy thực tế (empirical timing) thay cho Big-O?

\textbf{Trả lời:}
\begin{enumerate}
\item \textbf{Phụ thuộc phần cứng:} Cùng thuật toán, máy i9 chạy nhanh hơn máy Pentium gấp 100 lần -- thời gian thực tế không phản ánh bản chất thuật toán.
\item \textbf{Phụ thuộc input:} Thời gian chạy trên mảng 100 phần tử không nói gì về mảng $10^6$ phần tử. Big-O cho biết \textit{tốc độ tăng} khi input lớn dần.
\item \textbf{Tính phổ quát:} Big-O là ngôn ngữ chung, độc lập với ngôn ngữ lập trình, compiler, và hệ điều hành. $O(n \log n)$ luôn tốt hơn $O(n^2)$ khi $n$ đủ lớn, bất kể máy nào.
\item \textbf{Worst-case guarantee:} Đo thực tế chỉ cho kết quả trên 1 input cụ thể. Big-O đảm bảo cho \textbf{mọi} input.
\end{enumerate}

\subsubsection{Tự Trace 1.1 -- Loop Invariant: Điền 3 bước}\label{traceans:1.1}

\textbf{Câu hỏi:} Chứng minh Insertion Sort đúng bằng Loop Invariant.

\textbf{Trả lời:}
\begin{enumerate}
\item \textbf{Bất biến:} ``Tại đầu mỗi lần lặp for với $j$, \textit{mảng con $A[1..j-1]$ chứa các phần tử ban đầu của $A[1..j-1]$ nhưng đã được sắp xếp tăng dần}.''

\item \textbf{Initialization ($j=2$):} Mảng con $A[1..1]$ chỉ có 1 phần tử $\to$ đã sắp xếp. Bất biến đúng.

\item \textbf{Maintenance:} Giả sử $A[1..j-1]$ đã sắp. Khi xét $key = A[j]$, ta dịch các phần tử $> key$ sang phải và chèn $key$ vào đúng vị trí. Sau bước này, $A[1..j]$ đã sắp. Bất biến đúng trước lần lặp $j+1$.

\item \textbf{Termination:} Vòng lặp dừng khi $j = n+1$. Bất biến cho ta: $A[1..n]$ đã sắp tăng dần. $\square$
\end{enumerate}

% ============================================================
\subsection{Chương 2: Thuật toán Sắp xếp}

\subsubsection{Tại sao? 2.1 -- Merge Sort cần extra space mà Quick Sort thì không?}\label{whyans:2.1}

\textbf{Câu hỏi:} Tại sao Merge Sort cần $\Theta(n)$ extra space mà Quick Sort thì không?

\textbf{Trả lời:}
\begin{itemize}
\item \textbf{Merge Sort:} Bước \texttt{Merge} gộp 2 mảng con \textit{đã sắp} thành 1 mảng sắp. Để gộp, ta phải tạo mảng tạm chứa kết quả, vì không thể merge tại chỗ mà vẫn giữ $O(n)$. Merge in-place tồn tại nhưng phức tạp $O(n \log n)$ và hằng số rất lớn -- thực tế không ai dùng.
\item \textbf{Quick Sort:} Partition chỉ \textit{hoán đổi} phần tử trong chính mảng $A$ (swap $A[i] \leftrightarrow A[j]$), không cần mảng phụ. Chỉ dùng $O(\log n)$ stack cho đệ quy.
\end{itemize}

\subsubsection{Tự Trace 2.1 -- Insertion Sort: Trace mảng $[5, 3, 8, 1, 4]$}\label{traceans:2.1}

\textbf{Câu hỏi:} Trace Insertion Sort trên $A = [5, 3, 8, 1, 4]$.

\textbf{Trả lời:}

\begin{center}
\begin{tabular}{|c|c|l|}
\hline
\textbf{$j$} & \textbf{key} & \textbf{Mảng $A$ sau bước} \\
\hline
-- & -- & $[5, 3, 8, 1, 4]$ \\
\hline
2 & 3 & $[\mathbf{3}, 5, 8, 1, 4]$ \quad (3 < 5, dịch 5 sang phải, chèn 3) \\
\hline
3 & 8 & $[3, 5, \mathbf{8}, 1, 4]$ \quad (8 > 5, giữ nguyên) \\
\hline
4 & 1 & $[\mathbf{1}, 3, 5, 8, 4]$ \quad (1 < tất cả, dịch 3 phần tử, chèn 1 đầu) \\
\hline
5 & 4 & $[1, 3, \mathbf{4}, 5, 8]$ \quad (4 > 3, 4 < 5, chèn giữa) \\
\hline
\end{tabular}
\end{center}

\subsubsection{Tại sao? 2.2 -- Counting Sort không vi phạm cận dưới $\Omega(n \lg n)$?}\label{whyans:2.2}

\textbf{Câu hỏi:} Tại sao Counting Sort chạy $O(n+k)$ mà không vi phạm cận dưới $\Omega(n \lg n)$?

\textbf{Trả lời:} Cận dưới $\Omega(n \lg n)$ chỉ áp dụng cho thuật toán \textbf{dựa trên so sánh} (comparison-based), tức thuật toán chỉ dùng phép so sánh $<, >, =$ để quyết định thứ tự. Counting Sort \textbf{không so sánh} -- nó đếm số lần xuất hiện của mỗi giá trị rồi tính vị trí. Vì không thuộc mô hình ``decision tree'' nên không bị ràng buộc bởi $\Omega(n \lg n)$.

\textit{Đánh đổi:} Counting Sort cần biết phạm vi giá trị $k$ và tốn $\Theta(k)$ bộ nhớ phụ. Nếu $k \gg n$ (ví dụ: sắp xếp $n = 100$ số trong khoảng $[1, 10^9]$), Counting Sort không khả thi.

% ============================================================
\subsection{Chương 4: Lý thuyết Đồ thị}

\subsubsection{Tại sao? 4.1 -- Ma trận kề tốn $\Theta(V^2)$ dù đồ thị thưa?}\label{whyans:4.1}

\textbf{Câu hỏi:} Ma trận kề tốn $\Theta(V^2)$ bộ nhớ kể cả khi đồ thị rất thưa ($E \ll V^2$). Tại sao? Và tại sao danh sách kề chỉ tốn $\Theta(V+E)$?

\textbf{Trả lời:}
\begin{itemize}
\item \textbf{Ma trận kề:} Luôn cấp phát bảng $V \times V$, bất kể có bao nhiêu cạnh. Với 5 đỉnh, 3 cạnh: ta vẫn tạo bảng $5 \times 5 = 25$ ô, trong đó chỉ 3 ô $= 1$, còn lại 22 ô $= 0$ $\to$ \textbf{lãng phí}.
\item \textbf{Danh sách kề:} Mỗi đỉnh có 1 danh sách chỉ chứa các đỉnh kề. Tổng = $V$ danh sách + $2E$ phần tử (đồ thị vô hướng) hoặc $E$ phần tử (có hướng) = $\Theta(V+E)$.
\end{itemize}

\textbf{Ví dụ: 5 đỉnh, 3 cạnh} $\{(1,2), (2,3), (3,4)\}$:
\begin{itemize}
\item Ma trận: $5 \times 5 = 25$ ô, chỉ 6 ô $\neq 0$.
\item Danh sách kề: 5 heads + 6 entries = 11 phần tử. Tiết kiệm hơn hẳn!
\end{itemize}

% ============================================================
\subsection{Chương 5: Greedy -- MST}

\subsubsection{Tại sao? 5.1 -- Cạnh nhẹ nhất qua cut phải thuộc MST?}\label{whyans:5.1}

\textbf{Câu hỏi:} Tại sao cạnh nhẹ nhất qua một cut \textbf{phải} thuộc MST? (Cut Property)

\textbf{Trả lời (phản chứng):}
\begin{enumerate}
\item Giả sử $(u,v)$ là cạnh nhẹ nhất qua cut $(S, V \setminus S)$, nhưng $(u,v) \notin T^*$ (MST tối ưu).
\item Thêm $(u,v)$ vào $T^*$ $\to$ tạo đúng 1 chu trình (vì cây + 1 cạnh = 1 cycle).
\item Trong chu trình này, tồn tại cạnh khác $(x,y)$ cũng qua cut $(S, V \setminus S)$ (vì chu trình phải ``quay về'' phía bên kia cut).
\item Vì $(u,v)$ là cạnh \textbf{nhẹ nhất} qua cut: $w(u,v) \leq w(x,y)$.
\item Bỏ $(x,y)$, giữ $(u,v)$ $\to$ tạo cây $T' = T^* - \{(x,y)\} + \{(u,v)\}$ có tổng trọng số $\leq w(T^*)$.
\item Mà $T^*$ là MST $\to$ $w(T') = w(T^*)$ $\to$ $T'$ cũng là MST và chứa $(u,v)$. \textbf{Mâu thuẫn} với giả thiết ban đầu. $\square$
\end{enumerate}

\subsubsection{Tự Trace 5.1 -- Kruskal: Trace đồ thị 4 đỉnh}\label{traceans:5.1}

\textbf{Câu hỏi:} Cho đồ thị 4 đỉnh $\{1,2,3,4\}$ với cạnh: $(1,2,4)$, $(1,3,1)$, $(2,3,3)$, $(2,4,2)$, $(3,4,5)$.

\textbf{Trả lời:}

\textit{Sắp xếp cạnh tăng dần:} $(1,3,1)$, $(2,4,2)$, $(2,3,3)$, $(1,2,4)$, $(3,4,5)$.

\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Bước} & \textbf{Cạnh} & \textbf{$w$} & \textbf{Union-Find} & \textbf{Hành động} \\
\hline
1 & $(1,3)$ & 1 & $\{1,3\}, \{2\}, \{4\}$ & \cellcolor{green!15} Thêm vào MST \\
\hline
2 & $(2,4)$ & 2 & $\{1,3\}, \{2,4\}$ & \cellcolor{green!15} Thêm vào MST \\
\hline
3 & $(2,3)$ & 3 & $\{1,2,3,4\}$ & \cellcolor{green!15} Thêm vào MST \\
\hline
4 & $(1,2)$ & 4 & -- & \cellcolor{red!15} Bỏ (chu trình) \\
\hline
5 & $(3,4)$ & 5 & -- & \cellcolor{red!15} Bỏ (chu trình) \\
\hline
\end{tabular}
\end{center}

\textbf{MST:} $\{(1,3), (2,4), (2,3)\}$, tổng = $1 + 2 + 3 = \boxed{6}$.

% ============================================================
\subsection{Chương 6: Dijkstra}

\subsubsection{Tại sao? 6.1 -- Dijkstra không hoạt động với cạnh âm?}\label{whyans:6.1}

\textbf{Câu hỏi:} Tại sao Dijkstra không hoạt động với cạnh có trọng số âm? Xây dựng phản ví dụ.

\textbf{Trả lời:}

\textbf{Phản ví dụ:} 3 đỉnh $\{s, a, b\}$, cạnh: $s \to a (1)$, $s \to b (3)$, $b \to a (-4)$.

\begin{center}
\begin{tabular}{|c|c|c|c|c|l|}
\hline
\textbf{Bước} & $d[s]$ & $d[a]$ & $d[b]$ & \textbf{Extract} & \textbf{Ghi chú} \\
\hline
Init & \textbf{[0]} & $\infty$ & $\infty$ & $s$ & -- \\
\hline
1 & 0 & \textbf{[1]} & 3 & $a$ & $d[a]=1$, $d[b]=3$ \\
\hline
2 & 0 & 1 & \textbf{[3]} & $b$ & $b \to a$: $3+(-4)=-1 < 1$, nhưng $a$ đã ``khóa''! \\
\hline
\end{tabular}
\end{center}

Dijkstra cho $d[a] = 1$, nhưng đường đi thực sự ngắn nhất là $s \to b \to a = 3 + (-4) = -1$.

\textbf{Nguyên nhân:} Dijkstra giả định rằng khi đỉnh $u$ được ``khóa'' (extracted from Q), $d[u]$ là final. Với cạnh âm, giả định này \textbf{sai} -- có thể tìm đường ngắn hơn qua đỉnh chưa xử lý. Giải pháp: dùng \textbf{Bellman-Ford} ($O(VE)$).

\subsubsection{Tự Trace 6.1 -- Dijkstra: Trace bảng khoảng cách}\label{traceans:6.1}

\textbf{Câu hỏi:} Cho đồ thị 4 đỉnh $\{s,a,b,t\}$ với cạnh: $s{\to}a(1)$, $s{\to}b(4)$, $a{\to}b(2)$, $a{\to}t(6)$, $b{\to}t(3)$.

\textbf{Trả lời:}

\begin{center}
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Bước} & $d[s]$ & $d[a]$ & $d[b]$ & $d[t]$ & \textbf{ExtractMin} \\
\hline
Init & \cellcolor{green!15}\textbf{[0]} & $\infty$ & $\infty$ & $\infty$ & $s$ \\
\hline
1 & 0 & \cellcolor{green!15}\textbf{[1]} & 4 & $\infty$ & $a$ \\
\hline
2 & 0 & 1 & \cellcolor{green!15}\textbf{[3]} & 7 & $b$ \\
\hline
3 & 0 & 1 & 3 & \cellcolor{green!15}\textbf{[6]} & $t$ \\
\hline
\end{tabular}
\end{center}

\textbf{Chi tiết Relaxation:}
\begin{itemize}
\tightlist
\item Bước 1: Extract $s$. Relax $s{\to}a$: $d[a]=\min(\infty, 0+1)=1$. Relax $s{\to}b$: $d[b]=\min(\infty, 0+4)=4$.
\item Bước 2: Extract $a$. Relax $a{\to}b$: $d[b]=\min(4, 1+2)=3$. Relax $a{\to}t$: $d[t]=\min(\infty, 1+6)=7$.
\item Bước 3: Extract $b$. Relax $b{\to}t$: $d[t]=\min(7, 3+3)=6$.
\end{itemize}

Đường đi ngắn nhất $s \to t$: $s \to a \to b \to t$, chi phí $= 1 + 2 + 3 = \boxed{6}$.

% ============================================================
\subsection{Chương 7: Quy hoạch động -- Floyd-Warshall}

\subsubsection{Tại sao? 7.1 -- Floyd-Warshall: vòng lặp $k$ phải ở ngoài cùng?}\label{whyans:7.1}

\textbf{Câu hỏi:} Tại sao vòng lặp $k$ phải ở ngoài cùng? Nếu đặt $i$ hoặc $j$ ở ngoài thì sao?

\textbf{Trả lời:} Công thức Floyd-Warshall:
\[
D^{(k)}[i][j] = \min\left(D^{(k-1)}[i][j], \; D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\right)
\]

Ý nghĩa: $D^{(k)}[i][j]$ = đường đi ngắn nhất từ $i$ đến $j$ \textbf{chỉ dùng đỉnh trung gian trong tập $\{1, 2, \ldots, k\}$}.

\begin{itemize}
\item \textbf{$k$ ở ngoài cùng:} Mỗi lần tăng $k$, ta ``mở khóa'' thêm 1 đỉnh trung gian. Toàn bộ bảng $D^{(k)}$ được tính từ $D^{(k-1)}$ đã hoàn chỉnh $\to$ \textbf{đúng}.
\item \textbf{Nếu $i$ ở ngoài:} Khi tính $D[i][j]$ với $k$ nào đó, bảng $D[\cdot][k]$ và $D[k][\cdot]$ có thể chưa được cập nhật đầy đủ ở tầng $k$ hiện tại $\to$ sử dụng giá trị sai $\to$ \textbf{kết quả sai}.
\end{itemize}

\textit{Trực giác:} ``Mở khóa'' từng đỉnh trung gian theo thứ tự = xây dựng DP bottom-up đúng cách. Đảo thứ tự vòng lặp = phá vỡ thứ tự phụ thuộc DP.

"""

# Find the insertion point - right before \section{Phụ lục
insert_marker = r'\section{Phụ lục: Bảng tên gọi ký hiệu toán học}'
idx = content.find(insert_marker)
if idx == -1:
    print("ERROR: Could not find insertion point")
else:
    content = content[:idx] + solutions_chapter + "\n" + content[idx:]
    with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
        f.write(content)
    print(f"Inserted solutions chapter at position {idx}")
    print("Done")
