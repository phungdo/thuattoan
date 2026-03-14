import re

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Fix green cells that DON'T already have checkmark
# Pattern: \cellcolor{green!15} \textbf{Chọn} (without checkmark)
# But NOT: \cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{Chọn}
old_green = r'\cellcolor{green!15} \textbf{Chọn}'
new_green = r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{Chọn}'
count1 = content.count(old_green)
content = content.replace(old_green, new_green)

# Also handle Prim table: \cellcolor{green!15} \textbf{AB} etc.
# These are green cells with edge names, not "Chọn"
old_prim = lambda edge: f'\\cellcolor{{green!15}} \\textbf{{{edge}}}'
new_prim = lambda edge: f'\\cellcolor{{green!15}} \\textcolor{{green!50!black}}{{$\\checkmark$}} \\textbf{{{edge}}}'
count_prim = 0
for edge in ['AB', 'AC', 'CE', 'AD', 'CF', 'FG']:
    old = f'\\cellcolor{{green!15}} \\textbf{{{edge}}} '
    new = f'\\cellcolor{{green!15}} \\textcolor{{green!50!black}}{{$\\checkmark$}} \\textbf{{{edge}}} '
    c = content.count(old)
    content = content.replace(old, new)
    count_prim += c

# Fix red cells
old_red = r'\cellcolor{red!15} \textbf{Bỏ qua}'
new_red = r'\cellcolor{red!15} \textcolor{red!70!black}{$\times$} \textbf{Bỏ qua}'
count2 = content.count(old_red)
content = content.replace(old_red, new_red)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print(f"Replaced green 'Chọn': {count1}, green Prim edges: {count_prim}, red 'Bỏ qua': {count2}")
