with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# First remove duplicate Merge Sort LI + Complexity (lines around 781-800)
# There are TWO occurrences of "Loop Invariant (Merge):" and "Phân tích Complexity (Merge Sort):"
# Keep the first, remove the second
import re

# Find all occurrences of the Merge LI block
merge_li_text = "\\textbf{Loop Invariant (Merge):}"
positions = []
start = 0
while True:
    idx = content.find(merge_li_text, start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

if len(positions) > 1:
    # Remove from second occurrence to the next \subsubsection
    second_start = positions[1]
    # Find the start of the line before it (look for \n before)
    line_start = content.rfind('\n', 0, second_start)
    # Find the \subsubsection* that follows
    sub_marker = "\\subsubsection*{Minh họa Animation Merge Sort"
    sub_idx = content.find(sub_marker, second_start)
    if sub_idx:
        content = content[:line_start+1] + content[sub_idx:]
        print(f"Removed duplicate Merge LI+Complexity block")

# Now convert \textbf items to \subsubsection in sorting chapter
replacements = [
    # Bubble Sort
    ("\\textbf{Ý tưởng Bubble Sort:} So sánh", "\\subsubsection{Ý tưởng}\nSo sánh"),
    ("\\textbf{Complexity:} Worst/Average = $\\Theta(n^2)$. Best = $\\Theta(n)$", "\\subsubsection{Complexity}\nWorst/Average = $\\Theta(n^2)$. Best = $\\Theta(n)$"),
    ("\\textbf{Loop Invariant (Bubble Sort):}", "\\subsubsection{Loop Invariant}"),
    
    # Selection Sort
    ("\\textbf{Ý tưởng Selection Sort:} Duyệt", "\\subsubsection{Ý tưởng}\nDuyệt"),
    ("\\textbf{Complexity:} Worst/Average/Best = $\\Theta(n^2)$", "\\subsubsection{Complexity}\nWorst/Average/Best = $\\Theta(n^2)$"),
    ("\\textbf{Loop Invariant (Selection Sort):}", "\\subsubsection{Loop Invariant}"),
    
    # Insertion Sort  
    ("\\textbf{Ý tưởng Insertion Sort:} Giống", "\\subsubsection{Ý tưởng}\nGiống"),
    
    # Merge Sort
    ("\\textbf{Ý tưởng Merge Sort:} Áp dụng", "\\subsubsection{Ý tưởng}\nÁp dụng"),
    ("\\textbf{Loop Invariant (Merge):}", "\\subsubsection{Loop Invariant (Merge)}"),
    ("\\textbf{Phân tích Complexity (Merge Sort):}", "\\subsubsection{Phân tích Complexity}"),
    
    # Quick Sort
    ("\\textbf{Ý tưởng Quick Sort:} Chọn", "\\subsubsection{Ý tưởng}\nChọn"),
    ("\\textbf{Phân tích Complexity (Quick Sort):}", "\\subsubsection{Phân tích Complexity}"),
    
    # Heap Sort
    ("\\textbf{Complexity:} BuildMaxHeap = $O(n)$", "\\subsubsection{Complexity}\nBuildMaxHeap = $O(n)$"),
    ("\\textbf{Loop Invariant (HeapSort):}", "\\subsubsection{Loop Invariant}"),
    
    # Counting Sort
    ("\\textbf{Ý tưởng Counting Sort:} Thay", "\\subsubsection{Ý tưởng}\nThay"),
    ("\\textbf{Complexity:} $\\Theta(n + k)$ time", "\\subsubsection{Complexity}\n$\\Theta(n + k)$ time"),
    
    # Convert existing \subsubsection* (unnumbered) to \subsubsection (numbered)
    ("\\subsubsection*{Minh họa Animation Selection Sort (cùng mảng mẫu):}", "\\subsubsection{Minh họa Animation}"),
    ("\\subsubsection*{Minh họa Animation bằng từng bước (Step-by-step):}", "\\subsubsection{Minh họa Animation}"),
    ("\\subsubsection*{Minh họa Animation Merge Sort (cùng mảng mẫu):}", "\\subsubsection{Minh họa Animation}"),
    ("\\subsubsection*{Minh họa Animation Quick Sort đầy đủ (cùng mảng mẫu):}", "\\subsubsection{Minh họa Animation}"),
    ("\\subsubsection*{Minh họa Animation Heap Sort (cùng mảng mẫu):}", "\\subsubsection{Minh họa Animation}"),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)  # Replace only first occurrence
        print(f"  Replaced: {old[:50]}...")
    else:
        print(f"  NOT FOUND: {old[:50]}...")

# Also handle the Bubble Sort animation which is inside a tcolorbox
# It has "Minh họa Animation vòng lặp đầu tiên:" as \textbf
# Leave it as is since it's inside a box

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("\nDone!")
