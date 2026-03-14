import re

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# First remove duplicate Merge Sort blocks
# Find second occurrence of "Loop Invariant (Merge)" and remove up to Animation
merge_li = r'\textbf{Loop Invariant (Merge):}'
pos1 = content.find(merge_li)
pos2 = content.find(merge_li, pos1 + 1) if pos1 != -1 else -1
if pos2 != -1:
    # Find start of line
    line_start = content.rfind('\n', 0, pos2) + 1
    # Find next \subsubsection
    next_sub = content.find(r'\subsubsection', pos2)
    if next_sub != -1:
        content = content[:line_start] + content[next_sub:]
        print("Removed duplicate Merge LI+Complexity block")

# Now do replacements using regex to be more flexible
# Work within Chapter 2 only (between 2.2 Bubble Sort and Chương 3)
ch2_marker = r'\subsection{2.2 Bubble Sort}'
ch3_marker = r'\section{Chương 3:'
ch2_start = content.find(ch2_marker)
ch3_start = content.find(ch3_marker)

ch2 = content[ch2_start:ch3_start]

# Replacements within ch2
pairs = [
    # Bubble Sort items
    (r'\textbf{Ý tưởng Bubble Sort:}', r'\subsubsection{Ý tưởng}'),
    (r'\textbf{Complexity:} Worst/Average = $\Theta(n^2)$.', r'\subsubsection{Complexity}' + '\nWorst/Average = $\\Theta(n^2)$.'),
    (r'\textbf{Loop Invariant (Bubble Sort):}', r'\subsubsection{Loop Invariant}'),
    
    # Selection Sort items
    (r'\textbf{Ý tưởng Selection Sort:}', r'\subsubsection{Ý tưởng}'),
    (r'\subsubsection*{Minh họa Animation Selection Sort (cùng mảng mẫu):}', r'\subsubsection{Minh họa Animation}'),
    (r'\textbf{Complexity:} Worst/Average/Best = $\Theta(n^2)$', r'\subsubsection{Complexity}' + '\nWorst/Average/Best = $\\Theta(n^2)$'),
    (r'\textbf{Loop Invariant (Selection Sort):}', r'\subsubsection{Loop Invariant}'),
    
    # Insertion Sort items
    (r'\textbf{Ý tưởng Insertion Sort:}', r'\subsubsection{Ý tưởng}'),
    (r'\subsubsection*{Minh họa Animation bằng từng bước (Step-by-step):}', r'\subsubsection{Minh họa Animation}'),
    
    # Merge Sort items
    (r'\textbf{Ý tưởng Merge Sort:}', r'\subsubsection{Ý tưởng}'),
    (r'\textbf{Loop Invariant (Merge):}', r'\subsubsection{Loop Invariant (Merge)}'),
    (r'\textbf{Phân tích Complexity (Merge Sort):}', r'\subsubsection{Phân tích Complexity}'),
    (r'\subsubsection*{Minh họa Animation Merge Sort (cùng mảng mẫu):}', r'\subsubsection{Minh họa Animation}'),
    
    # Quick Sort items
    (r'\textbf{Ý tưởng Quick Sort:}', r'\subsubsection{Ý tưởng}'),
    (r'\textbf{Phân tích Complexity (Quick Sort):}', r'\subsubsection{Phân tích Complexity}'),
    (r'\subsubsection*{Minh họa Animation Quick Sort đầy đủ (cùng mảng mẫu):}', r'\subsubsection{Minh họa Animation}'),
    
    # Heap Sort items
    (r'\textbf{Complexity:} BuildMaxHeap = $O(n)$.', r'\subsubsection{Complexity}' + '\nBuildMaxHeap = $O(n)$.'),
    (r'\textbf{Loop Invariant (HeapSort):}', r'\subsubsection{Loop Invariant}'),
    (r'\subsubsection*{Minh họa Animation Heap Sort (cùng mảng mẫu):}', r'\subsubsection{Minh họa Animation}'),
    
    # Counting Sort items
    (r'\textbf{Ý tưởng Counting Sort:}', r'\subsubsection{Ý tưởng}'),
    (r'\textbf{Complexity:} $\Theta(n + k)$ time,', r'\subsubsection{Complexity}' + '\n$\\Theta(n + k)$ time,'),
]

for old, new in pairs:
    if old in ch2:
        ch2 = ch2.replace(old, new, 1)
        print(f"  OK: {old[:50]}...")
    else:
        print(f"  MISS: {old[:50]}...")

content = content[:ch2_start] + ch2 + content[ch3_start:]

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("\nDone!")
