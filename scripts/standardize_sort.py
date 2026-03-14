with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# 1. BUBBLE SORT: Add Pseudocode + Complexity AFTER the tcolorbox ends (line 555-556)
# Insert after \end{tcolorbox}\n\vspace{0.3cm} and before Selection Sort
bubble_insert_marker = "\\end{tcolorbox}\n\\vspace{0.3cm}\n\n\\subsection{2.3 Selection Sort}"
bubble_addition = """\\end{tcolorbox}

\\begin{tcolorbox}[colback=gray!8, colframe=gray!50, boxrule=0.5pt, arc=2pt,
  left=6pt, right=6pt, top=4pt, bottom=4pt,
  title={\\small\\textbf{Pseudocode 3a: Bubble Sort}}]
\\begin{verbatim}
BubbleSort(A, n):
    for i = 1 to n-1:
        for j = 1 to n-i:
            if A[j] > A[j+1]:
                swap(A[j], A[j+1])
\\end{verbatim}
\\end{tcolorbox}

\\textbf{Complexity:} Worst/Average = $\\Theta(n^2)$. Best = $\\Theta(n)$ nếu thêm cờ ``đã sắp'' (early termination). Space = $O(1)$ (in-place). Stable.

\\subsection{2.3 Selection Sort}"""
content = content.replace(bubble_insert_marker, bubble_addition)

# 2. SELECTION SORT: Add Pseudocode + Complexity AFTER the animation figure, BEFORE Insertion Sort
sel_insert_marker = "\\captionof{figure}{Selection Sort -- Toàn bộ quá trình sắp xếp trên mảng $[5, 3, 8, 1, 4]$}\\label{fig:selection-sort}\n\n\\subsection"
sel_addition = """\\captionof{figure}{Selection Sort -- Toàn bộ quá trình sắp xếp trên mảng $[5, 3, 8, 1, 4]$}\\label{fig:selection-sort}

\\begin{tcolorbox}[colback=gray!8, colframe=gray!50, boxrule=0.5pt, arc=2pt,
  left=6pt, right=6pt, top=4pt, bottom=4pt,
  title={\\small\\textbf{Pseudocode 3b: Selection Sort}}]
\\begin{verbatim}
SelectionSort(A, n):
    for i = 1 to n-1:
        min_idx = i
        for j = i+1 to n:
            if A[j] < A[min_idx]:
                min_idx = j
        swap(A[i], A[min_idx])
\\end{verbatim}
\\end{tcolorbox}

\\textbf{Complexity:} Worst/Average/Best = $\\Theta(n^2)$ (luôn quét toàn bộ phần còn lại). Space = $O(1)$ (in-place). \\textbf{Không stable} (swap có thể đổi thứ tự tương đối).

\\subsection"""
content = content.replace(sel_insert_marker, sel_addition)

# 3. INSERTION SORT: Add Ý tưởng BEFORE Pseudocode
ins_marker = "\\subsection{\\texorpdfstring{2.4 Insertion Sort"
ins_end = "\\begin{tcolorbox}[colback=gray!8, colframe=gray!50, boxrule=0.5pt, arc=2pt,\n  left=6pt, right=6pt, top=4pt, bottom=4pt,\n  title={\\small\\textbf{Pseudocode 4: Insertion Sort}}]"
ins_replacement = """\\textbf{Ý tưởng Insertion Sort:} Giống cách xếp bài trên tay: lấy từng lá bài (phần tử $A[j]$) và \\textbf{chèn} vào đúng vị trí trong phần đã sắp $A[1..j-1]$. Dịch các phần tử lớn hơn sang phải để tạo chỗ. Hiệu quả trên mảng \\textbf{gần sắp} (best case $\\Theta(n)$), nhưng worst case $\\Theta(n^2)$.

\\begin{tcolorbox}[colback=gray!8, colframe=gray!50, boxrule=0.5pt, arc=2pt,
  left=6pt, right=6pt, top=4pt, bottom=4pt,
  title={\\small\\textbf{Pseudocode 4: Insertion Sort}}]"""
content = content.replace(ins_end, ins_replacement)

# 4. MERGE SORT: Add Ý tưởng BEFORE "Mô hình D&C"
merge_marker = "\\textbf{Mô hình D\\&C (CLRS \\S 2.3.1):}"
merge_replacement = """\\textbf{Ý tưởng Merge Sort:} Áp dụng Divide \\& Conquer: chia mảng thành 2 nửa bằng nhau, đệ quy sắp xếp từng nửa, rồi \\textbf{trộn (merge)} 2 nửa đã sắp thành mảng hoàn chỉnh. Công việc nặng nằm ở bước \\textit{trộn}, cần mảng tạm $O(n)$. Luôn $\\Theta(n \\lg n)$ bất kể input, nhưng \\textbf{không in-place} (tốn thêm bộ nhớ).

\\textbf{Mô hình D\\&C (CLRS \\S 2.3.1):}"""
content = content.replace(merge_marker, merge_replacement)

# 5. COUNTING SORT: Create section 2.8 -- insert BEFORE Heap Sort's whyprompt
# Find the Counting Sort ý tưởng text and checkpoint that are currently between Quick Sort and Heap Sort
# Currently: Counting Sort text -> whyprompt -> checkpoint -> Heap Sort
counting_marker = "\\textbf{Ý tưởng Counting Sort} (CLRS Ch.8):"
counting_old = """\\textbf{Ý tưởng Counting Sort} (CLRS Ch.8): Thay vì so sánh, ta \\textbf{đếm} số lần xuất hiện của mỗi giá trị. Tạo mảng đếm $C[0..k]$, với $C[x]$ = số phần tử $= x$. Cộng dồn $C$ để biết vị trí cuối cùng của mỗi giá trị trong output. Duyệt ngược mảng gốc, đặt từng phần tử vào đúng vị trí $\\to$ \\textbf{stable}, $O(n+k)$. Chỉ dùng khi biết phạm vi giá trị $k$ và $k$ không quá lớn.

\\whyprompt{Tại sao \\textbf{Counting Sort} không vi phạm cận dưới $\\Omega(n \\lg n)$, dù nó chạy $O(n+k)$? Gợi ý: xem lại điều kiện ``sắp xếp dựa trên so sánh'' trong Theorem 8.1 (CLRS).}

\\checkpoint{Độ phức tạp worst case của Quick Sort là gì? Tại sao trong thực tế ta vẫn dùng Quick Sort thay vì Merge Sort? (Nêu 2 lý do.)}

\\subsection{2.7 Heap Sort"""
counting_new = """\\checkpoint{Độ phức tạp worst case của Quick Sort là gì? Tại sao trong thực tế ta vẫn dùng Quick Sort thay vì Merge Sort? (Nêu 2 lý do.)}

\\subsection{2.7 Heap Sort"""
content = content.replace(counting_old, counting_new)

# Now insert section 2.8 Counting Sort AFTER Heap Sort section ends (before the rule/section break)
# Find the end of Heap Sort animation and insert Counting Sort
heap_end_marker = "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Chương 3:"
counting_section = """\\subsection{2.8 Counting Sort -- CLRS Ch.8}\\label{counting-sort}

\\textbf{Ý tưởng Counting Sort:} Thay vì so sánh, ta \\textbf{đếm} số lần xuất hiện của mỗi giá trị. Tạo mảng đếm $C[0..k]$, với $C[x]$ = số phần tử $= x$. Cộng dồn $C$ để biết vị trí cuối cùng của mỗi giá trị trong output. Duyệt ngược mảng gốc, đặt từng phần tử vào đúng vị trí $\\to$ \\textbf{stable}, $O(n+k)$. Chỉ dùng khi biết phạm vi giá trị $k$ và $k$ không quá lớn.

\\begin{tcolorbox}[colback=gray!8, colframe=gray!50, boxrule=0.5pt, arc=2pt,
  left=6pt, right=6pt, top=4pt, bottom=4pt,
  title={\\small\\textbf{Pseudocode 9: Counting Sort (CLRS 8.2)}}]
\\begin{verbatim}
CountingSort(A, B, n, k):
    // A: input, B: output, k: max value
    let C[0..k] = all zeros
    for j = 1 to n:
        C[A[j]] = C[A[j]] + 1      // dem tan suat
    for i = 1 to k:
        C[i] = C[i] + C[i-1]       // cong don -> vi tri
    for j = n downto 1:             // duyet NGUOC -> stable
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
\\end{verbatim}
\\end{tcolorbox}

\\textbf{Complexity:} $\\Theta(n + k)$ time, $\\Theta(n + k)$ space. Stable. \\textbf{Không dựa trên so sánh} -- vì vậy không bị ràng buộc bởi cận dưới $\\Omega(n \\lg n)$.

\\whyprompt{Tại sao \\textbf{Counting Sort} không vi phạm cận dưới $\\Omega(n \\lg n)$, dù nó chạy $O(n+k)$? Gợi ý: xem lại điều kiện ``sắp xếp dựa trên so sánh'' trong Theorem 8.1 (CLRS).}

\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}

\\section{Chương 3:"""
content = content.replace(heap_end_marker, counting_section)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("Done - standardized all sorting algorithms")
