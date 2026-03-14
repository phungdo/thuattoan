with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# 1. BUBBLE SORT: Add Loop Invariant after Complexity (line 569)
bubble_cx = "\\textbf{Complexity:} Worst/Average = $\\Theta(n^2)$. Best = $\\Theta(n)$ nếu thêm cờ ``đã sắp'' (early termination). Space = $O(1)$ (in-place). Stable.\n\n\\subsection{2.3 Selection Sort}"

bubble_li = """\\textbf{Complexity:} Worst/Average = $\\Theta(n^2)$. Best = $\\Theta(n)$ nếu thêm cờ ``đã sắp'' (early termination). Space = $O(1)$ (in-place). Stable.

\\textbf{Loop Invariant (Bubble Sort):}
\\begin{itemize}
\\tightlist
\\item \\textbf{Bất biến:} Sau vòng lặp ngoài thứ $i$, $i$ phần tử lớn nhất đã nằm đúng vị trí cuối mảng $A[n{-}i{+}1..n]$, đã sắp.
\\item \\textbf{Init ($i=1$):} Chưa vòng nào chạy, chưa phần tử nào ``cố định'' -- bất biến đúng (trivial).
\\item \\textbf{Maintenance:} Vòng $i$ so sánh các cặp kề $A[j], A[j{+}1]$. Swap nếu sai thứ tự $\\to$ phần tử lớn nhất trong $A[1..n{-}i{+}1]$ ``nổi'' lên vị trí $n{-}i{+}1$. Sau vòng $i$: $i$ phần tử lớn nhất đã cố định.
\\item \\textbf{Termination ($i=n{-}1$):} $n{-}1$ phần tử lớn nhất đã đúng chỗ $\\to$ phần tử còn lại (nhỏ nhất) cũng đúng $\\to$ mảng sắp. $\\square$
\\end{itemize}

\\subsection{2.3 Selection Sort}"""
content = content.replace(bubble_cx, bubble_li)

# 2. SELECTION SORT: Add Loop Invariant after Complexity (line 613)
sel_cx = "\\textbf{Complexity:} Worst/Average/Best = $\\Theta(n^2)$ (luôn quét toàn bộ phần còn lại). Space = $O(1)$ (in-place). \\textbf{Không stable} (swap có thể đổi thứ tự tương đối).\n\n\\subsection"

sel_li = """\\textbf{Complexity:} Worst/Average/Best = $\\Theta(n^2)$ (luôn quét toàn bộ phần còn lại). Space = $O(1)$ (in-place). \\textbf{Không stable} (swap có thể đổi thứ tự tương đối).

\\textbf{Loop Invariant (Selection Sort):}
\\begin{itemize}
\\tightlist
\\item \\textbf{Bất biến:} Tại đầu vòng lặp $i$, mảng con $A[1..i{-}1]$ chứa $i{-}1$ phần tử nhỏ nhất của mảng, đã sắp tăng dần.
\\item \\textbf{Init ($i=1$):} $A[1..0]$ rỗng -- bất biến đúng (trivial).
\\item \\textbf{Maintenance:} Tìm min trong $A[i..n]$, swap về vị trí $i$. $A[i]$ giờ là phần tử nhỏ nhất trong phần còn lại, và $\\geq$ tất cả $A[1..i{-}1]$ $\\to$ $A[1..i]$ đã sắp.
\\item \\textbf{Termination ($i=n$):} $A[1..n{-}1]$ chứa $n{-}1$ phần tử nhỏ nhất, đã sắp. Phần tử $A[n]$ là lớn nhất $\\to$ mảng sắp. $\\square$
\\end{itemize}

\\subsection"""
content = content.replace(sel_cx, sel_li)

# 3. MERGE SORT: Add Loop Invariant + Complexity before Animation
merge_anim = "\\subsubsection*{Minh họa Animation Merge Sort (cùng mảng mẫu):}"

merge_li_cx = """\\textbf{Loop Invariant (Merge):}
\\begin{itemize}
\\tightlist
\\item \\textbf{Bất biến:} Tại đầu mỗi lần lặp của vòng for trong \\texttt{Merge}, mảng con output $A[p..k{-}1]$ chứa $k{-}p$ phần tử nhỏ nhất của 2 mảng con $L$ và $R$, đã sắp tăng dần.
\\item \\textbf{Init ($k=p$):} $A[p..p{-}1]$ rỗng -- bất biến đúng.
\\item \\textbf{Maintenance:} So sánh đầu $L$ và đầu $R$, chọn phần tử nhỏ hơn đặt vào $A[k]$. Phần tử này $\\geq$ tất cả phần tử đã đặt (vì $L, R$ đã sắp) $\\to$ $A[p..k]$ vẫn sắp.
\\item \\textbf{Termination:} Khi hết cả $L$ lẫn $R$, $A[p..r]$ chứa tất cả phần tử ban đầu, đã sắp. $\\square$
\\end{itemize}

\\textbf{Phân tích Complexity (Merge Sort):}
\\begin{itemize}
\\tightlist
\\item \\textbf{Divide:} Chia đôi = $\\Theta(1)$.
\\item \\textbf{Conquer:} $2$ bài con kích thước $n/2$ = $2T(n/2)$.
\\item \\textbf{Combine (Merge):} Trộn 2 mảng đã sắp = $\\Theta(n)$.
\\item \\textbf{Recurrence:} $T(n) = 2T(n/2) + \\Theta(n)$. Áp dụng Master Theorem Case 2: $a=2, b=2, f(n)=\\Theta(n)=\\Theta(n^{\\log_2 2})$ $\\to$ $T(n) = \\Theta(n \\lg n)$.
\\item \\textbf{Space:} $\\Theta(n)$ (mảng tạm cho Merge) + $\\Theta(\\lg n)$ (stack đệ quy) = $\\Theta(n)$.
\\item Worst = Average = Best = $\\Theta(n \\lg n)$. \\textbf{Stable}. Không in-place.
\\end{itemize}

\\subsubsection*{Minh họa Animation Merge Sort (cùng mảng mẫu):}"""
content = content.replace(merge_anim, merge_li_cx)

# 4. QUICK SORT: Add Complexity after Randomized section
qs_post = "Chọn pivot \\textbf{ngẫu nhiên} \\(\\to\\) Expected time =\n\\(\\Theta(n \\lg n)\\), tránh worst case có hệ thống.\n\n\\checkpoint"

qs_cx = """Chọn pivot \\textbf{ngẫu nhiên} \\(\\to\\) Expected time =
\\(\\Theta(n \\lg n)\\), tránh worst case có hệ thống.

\\textbf{Phân tích Complexity (Quick Sort):}
\\begin{itemize}
\\tightlist
\\item \\textbf{Best case:} Partition chia đều $\\to$ $T(n) = 2T(n/2) + \\Theta(n) = \\Theta(n \\lg n)$.
\\item \\textbf{Worst case:} Pivot luôn là min/max (mảng đã sắp + pivot cuối) $\\to$ $T(n) = T(n{-}1) + \\Theta(n) = \\Theta(n^2)$.
\\item \\textbf{Average case:} Phân tích bằng indicator random variables: mọi cách chia đều cho $\\Theta(n \\lg n)$ trung bình.
\\item \\textbf{Space:} $O(\\lg n)$ avg (stack đệ quy), $O(n)$ worst case. In-place (không cần mảng phụ). \\textbf{Không stable}.
\\end{itemize}

\\checkpoint"""
content = content.replace(qs_post, qs_cx)

# 5. HEAP SORT: Add Loop Invariant after Complexity
heap_cx = "\\textbf{Complexity:} BuildMaxHeap = $O(n)$. HeapSort = $\\Theta(n \\lg n)$ (worst, average, best). Space = $O(1)$ (in-place). Không stable.\n\n\\subsubsection*{Minh họa Animation Heap Sort"

heap_li = """\\textbf{Complexity:} BuildMaxHeap = $O(n)$. HeapSort = $\\Theta(n \\lg n)$ (worst, average, best). Space = $O(1)$ (in-place). Không stable.

\\textbf{Loop Invariant (HeapSort):}
\\begin{itemize}
\\tightlist
\\item \\textbf{Bất biến:} Tại đầu mỗi lần lặp \\texttt{for i = n downto 2}: (1) $A[1..i]$ là max-heap, và (2) $A[i{+}1..n]$ chứa $n{-}i$ phần tử lớn nhất của mảng, đã sắp tăng dần.
\\item \\textbf{Init ($i=n$):} BuildMaxHeap vừa chạy xong $\\to$ $A[1..n]$ là max-heap. $A[n{+}1..n]$ rỗng -- bất biến đúng.
\\item \\textbf{Maintenance:} $A[1]$ = max của heap $\\to$ swap $A[1] \\leftrightarrow A[i]$ $\\to$ $A[i]$ đúng chỗ. Gọi MaxHeapify$(A, 1, i{-}1)$ để sửa heap. Bất biến đúng cho $i{-}1$.
\\item \\textbf{Termination ($i=1$):} $A[2..n]$ chứa $n{-}1$ phần tử lớn nhất, sắp. $A[1]$ là nhỏ nhất $\\to$ mảng sắp. $\\square$
\\end{itemize}

\\subsubsection*{Minh họa Animation Heap Sort"""
content = content.replace(heap_cx, heap_li)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("Done - added Loop Invariant + Complexity for all sorting algorithms")
