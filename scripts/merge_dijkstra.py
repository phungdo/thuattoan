with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

# Find Pseudocode 16 block (lines 1711-1727, 0-indexed 1710-1726)
ps16_start = None
ps16_end = None
for i, line in enumerate(lines):
    if 'Pseudocode 16: Dijkstra' in line:
        # Go back to find the tcolorbox start
        for j in range(i, max(i-5, 0), -1):
            if 'begin{tcolorbox}' in lines[j]:
                ps16_start = j
                break
        break

for i in range(ps16_start, min(ps16_start + 25, len(lines))):
    if 'end{tcolorbox}' in lines[i]:
        ps16_end = i
        break

# Find Manning-style section (lines 1894-1941)
manning_start = None
manning_end = None
for i, line in enumerate(lines):
    if 'MANNING-STYLE ANNOTATED DIJKSTRA' in line:
        manning_start = i
        break

for i in range(manning_start, min(manning_start + 60, len(lines))):
    if '\\end{tikzpicture}' in lines[i] and i > manning_start + 10:
        # Find the \end{center} after it
        for j in range(i, min(i + 5, len(lines))):
            if '\\end{center}' in lines[j]:
                manning_end = j
                break
        break

print(f"Pseudocode 16: lines {ps16_start+1}-{ps16_end+1}")
print(f"Manning section: lines {manning_start+1}-{manning_end+1}")

# Extract the Manning annotated content (just the tikzpicture part, keeping title)
manning_content = lines[manning_start:manning_end+1]

# Replace Pseudocode 16 with Manning content, keeping Pseudocode 16 numbering in title
new_block = """% ===== DIJKSTRA PSEUDOCODE WITH ANNOTATIONS =====
\\begin{center}
\\begin{tikzpicture}[remember picture]
\\node[text width=0.55\\linewidth, anchor=north west, inner sep=0] (code) at (0,0) {
\\begin{lstlisting}[escapechar=|]
Dijkstra(G, w, s):
    for moi v in V:|\\tikzmark{init}|
        d[v] = INF;  pi[v] = NIL
    d[s] = 0|\\tikzmark{source}|
    S = empty
    Q = MinPriorityQueue(V, d)|\\tikzmark{queue}|
    while Q != empty:
        u = ExtractMin(Q)|\\tikzmark{greedy}|
        S = S + {u}
        for moi v in Adj[u]:|\\tikzmark{relax}|
            Relax(u, v, w)
\\end{lstlisting}
};

% Right-side annotations with arrows
\\node[text width=4.8cm, anchor=west, font=\\small\\itshape, text=blue!70!black]
  (n1) at ([xshift=0.56\\linewidth, yshift=-0.3cm]code.north west)
  {Khởi tạo mọi đỉnh: khoảng cách $= \\infty$, cha $=$ NIL};
\\draw[-{Stealth[length=4pt]}, blue!50, thick]
  (n1.west) -- ([xshift=0.54\\linewidth, yshift=-0.3cm]code.north west);

\\node[text width=4.8cm, anchor=west, font=\\small\\itshape, text=green!60!black]
  (n2) at ([xshift=0.56\\linewidth, yshift=-1.1cm]code.north west)
  {Đỉnh nguồn có $d[s]=0$ -- điểm xuất phát};
\\draw[-{Stealth[length=4pt]}, green!50!black, thick]
  (n2.west) -- ([xshift=0.54\\linewidth, yshift=-1.1cm]code.north west);

\\node[text width=4.8cm, anchor=west, font=\\small\\itshape, text=red!70!black]
  (n3) at ([xshift=0.56\\linewidth, yshift=-2.1cm]code.north west)
  {\\textbf{GREEDY:} Luôn chọn đỉnh gần nhất -- bất biến cốt lõi};
\\draw[-{Stealth[length=4pt]}, red!60, thick]
  (n3.west) -- ([xshift=0.54\\linewidth, yshift=-2.1cm]code.north west);

\\node[text width=4.8cm, anchor=west, font=\\small\\itshape, text=violet!70!black]
  (n4) at ([xshift=0.56\\linewidth, yshift=-3.0cm]code.north west)
  {\\textbf{DP update:} Cập nhật $d[v]$ nếu tìm đường ngắn hơn qua $u$};
\\draw[-{Stealth[length=4pt]}, violet!60, thick]
  (n4.west) -- ([xshift=0.54\\linewidth, yshift=-3.0cm]code.north west);
\\end{tikzpicture}
\\end{center}
"""

# Replace Pseudocode 16 block
lines[ps16_start:ps16_end+1] = [new_block]

# Recalculate Manning section position (it shifted)
# Find it again
manning_start2 = None
manning_end2 = None
for i, line in enumerate(lines):
    if 'MANNING-STYLE ANNOTATED DIJKSTRA' in line:
        manning_start2 = i
        break

if manning_start2:
    for i in range(manning_start2, min(manning_start2 + 60, len(lines))):
        if '\\end{center}' in lines[i] and i > manning_start2 + 10:
            manning_end2 = i
            break

    # Find the subsubsection header before it
    for j in range(manning_start2, max(manning_start2 - 5, 0), -1):
        if 'subsubsection' in lines[j] and 'chú thích' in lines[j]:
            manning_start2 = j
            break
        if lines[j].strip() == '' and j < manning_start2:
            pass

    print(f"Removing duplicate Manning: lines {manning_start2+1}-{manning_end2+1}")
    del lines[manning_start2:manning_end2+1]

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print("Done")
