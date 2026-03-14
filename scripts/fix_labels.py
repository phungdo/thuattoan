with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Remove checkmark symbols from green cells
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{Chọn}',
    r'\cellcolor{green!15} \textbf{Thêm vào MST}'
)

# Remove cross symbols from red cells  
content = content.replace(
    r'\cellcolor{red!15} \textcolor{red!70!black}{$\times$} \textbf{Bỏ qua}',
    r'\cellcolor{red!15} \textbf{Bỏ (chu trình)}'
)

# Fix Prim table - remove checkmarks from edge selections
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{AB} (2)',
    r'\cellcolor{green!15} \textbf{AB} (2)'
)
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{AC} (3)',
    r'\cellcolor{green!15} \textbf{AC} (3)'
)
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{CE} (1)',
    r'\cellcolor{green!15} \textbf{CE} (1)'
)
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{AD} (3)',
    r'\cellcolor{green!15} \textbf{AD} (3)'
)
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{CF} (6)',
    r'\cellcolor{green!15} \textbf{CF} (6)'
)
content = content.replace(
    r'\cellcolor{green!15} \textcolor{green!50!black}{$\checkmark$} \textbf{FG} (9)',
    r'\cellcolor{green!15} \textbf{FG} (9)'
)

# Update Kruskal table header to be clearer
content = content.replace(
    r'\textbf{Hành động}',
    r'\textbf{Cạnh $\to$ MST?}'
)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print("Done")
