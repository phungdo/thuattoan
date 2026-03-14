with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Add checkmark to green cells  
old_green = r'\cellcolor{green!15} \textbf{Chọn}'
new_green = r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{Chọn}'
count1 = content.count(old_green)
content = content.replace(old_green, new_green)

# Add X to red cells
old_red = r'\cellcolor{red!15} \textbf{Bỏ qua}'
new_red = r'\cellcolor{red!15} \textcolor{red!70!black}{$\times$} \textbf{Bỏ qua}'
count2 = content.count(old_red)
content = content.replace(old_red, new_red)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print(f"Replaced {count1} green cells, {count2} red cells")
