with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

# Find start line (1761 in 1-indexed = index 1760)
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if 'Ví dụ 8 đỉnh' in line:
        start_idx = i
    if start_idx is not None and '\\end{longtable}' in line:
        end_idx = i
        break

# Also get the closing } on the next non-empty line
if end_idx is not None:
    for i in range(end_idx + 1, min(end_idx + 5, len(lines))):
        if lines[i].strip() == '}':
            end_idx = i
            break

print(f"Replacing lines {start_idx+1} to {end_idx+1}")

new_content = r"""\subsubsection{Minh họa trực quan Dijkstra (Visual Trace -- đồ thị giống video YouTube):}

\begin{center}
\textit{Video hướng dẫn:} \href{https://www.youtube.com/watch?v=_lHSawdgXpI}{\textcolor{blue}{\underline{Dijkstra's Algorithm -- YouTube (click để xem)}}}
\end{center}

Cho đồ thị \textbf{có hướng} $G$ với $V = \{A, B, C, D, E\}$, nguồn $s = A$:

\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|}
\hline
Cạnh & A$\to$B & A$\to$C & B$\to$C & B$\to$D & B$\to$E & C$\to$B & C$\to$D & C$\to$E & E$\to$D \\
\hline
$w$ & 4 & 2 & 3 & 2 & 3 & 1 & 4 & 5 & 1 \\
\hline
\end{tabular}
\end{center}

\begin{center}
\begin{minipage}[t]{0.48\textwidth}
\centering
\begin{tikzpicture}[
  vertex/.style={circle, draw, thick, minimum size=7mm, font=\bfseries\small},
  edge label/.style={rectangle, draw=none, fill=white, font=\scriptsize, inner sep=1pt},
  >=Stealth, scale=0.9, transform shape
]
  \node[vertex, draw=red, text=red] (A) at (0, 1.5) {A};
  \node[vertex] (B) at (2, 3)   {B};
  \node[vertex] (C) at (2, 0)   {C};
  \node[vertex] (D) at (5, 3)   {D};
  \node[vertex] (E) at (5, 0)   {E};
  % Directed edges
  \draw[->, thick] (A) -- node[edge label, above left] {4} (B);
  \draw[->, thick] (A) -- node[edge label, below left] {2} (C);
  \draw[->, thick] (B) -- node[edge label, right] {3} (C);
  \draw[->, thick] (B) -- node[edge label, above] {2} (D);
  \draw[->, thick, shorten >=2pt] (B) -- node[edge label, below, pos=0.4] {3} (E);
  \draw[->, thick] (C) -- node[edge label, left] {1} (B);
  \draw[->, thick, shorten >=2pt] (C) -- node[edge label, above, pos=0.4] {4} (D);
  \draw[->, thick] (C) -- node[edge label, below] {5} (E);
  \draw[->, thick] (E) -- node[edge label, right] {1} (D);
\end{tikzpicture}
\captionof{figure}{(a) Đồ thị gốc $G$ -- 9 cạnh có hướng}\label{fig:dijkstra-graph}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.48\textwidth}
\centering
\begin{tikzpicture}[
  vertex/.style={circle, draw=red!80!black, thick, text=red!80!black, minimum size=7mm, font=\bfseries\small},
  edge label/.style={rectangle, draw=none, fill=white, font=\scriptsize, inner sep=1pt, text=red!80!black},
  >=Stealth, scale=0.9, transform shape
]
  \node[vertex] (A) at (0, 1.5) {A};
  \node[vertex] (B) at (2, 3)   {B};
  \node[vertex] (C) at (2, 0)   {C};
  \node[vertex] (D) at (5, 3)   {D};
  \node[vertex] (E) at (5, 0)   {E};
  % Shortest path tree edges only
  \draw[->, very thick, red!80!black] (A) -- node[edge label, below left] {2} (C);
  \draw[->, very thick, red!80!black] (C) -- node[edge label, left] {1} (B);
  \draw[->, very thick, red!80!black] (B) -- node[edge label, above] {2} (D);
  \draw[->, very thick, red!80!black] (B) -- node[edge label, below, pos=0.4] {3} (E);
  % Distance labels
  \node[font=\scriptsize\bfseries, text=blue!70!black] at (0, 0.7) {$d=0$};
  \node[font=\scriptsize\bfseries, text=blue!70!black] at (2, 3.6) {$d=3$};
  \node[font=\scriptsize\bfseries, text=blue!70!black] at (2, -0.6) {$d=2$};
  \node[font=\scriptsize\bfseries, text=blue!70!black] at (5, 3.6) {$d=5$};
  \node[font=\scriptsize\bfseries, text=blue!70!black] at (5, -0.6) {$d=6$};
\end{tikzpicture}
\captionof{figure}{(b) Cây đường đi ngắn nhất từ $A$}\label{fig:dijkstra-spt}
\end{minipage}
\end{center}

\textbf{Trace Dijkstra từ $s = A$:}

\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|l|}
\hline
\textbf{Bước} & $d[A]$ & $d[B]$ & $d[C]$ & $d[D]$ & $d[E]$ & \textbf{ExtractMin} & \textbf{Relaxation} \\
\hline
Init & \cellcolor{green!15}\textbf{[0]} & $\infty$ & $\infty$ & $\infty$ & $\infty$ & $A$ & -- \\
\hline
1 & 0 & 4 & \cellcolor{green!15}\textbf{[2]} & $\infty$ & $\infty$ & $C$ & \small A$\to$B: $d[B]=4$, A$\to$C: $d[C]=2$ \\
\hline
2 & 0 & \cellcolor{green!15}\textbf{[3]} & 2 & 6 & 7 & $B$ & \small C$\to$B: $\min(4, 2{+}1){=}3$, C$\to$D: $6$, C$\to$E: $7$ \\
\hline
3 & 0 & 3 & 2 & \cellcolor{green!15}\textbf{[5]} & 6 & $D$ & \small B$\to$D: $\min(6, 3{+}2){=}5$, B$\to$E: $\min(7, 3{+}3){=}6$ \\
\hline
4 & 0 & 3 & 2 & 5 & \cellcolor{green!15}\textbf{[6]} & $E$ & \small E$\to$D: $6{+}1{=}7 > 5$, no change \\
\hline
\end{tabular}
\end{center}

\textbf{Kết quả:} $d[A]=0$, $d[B]=3$, $d[C]=2$, $d[D]=5$, $d[E]=6$.

\textbf{Đường đi ngắn nhất:}
\begin{itemize}
\tightlist
\item $A \to C$: chi phí $= 2$ (trực tiếp)
\item $A \to C \to B$: chi phí $= 2 + 1 = 3$
\item $A \to C \to B \to D$: chi phí $= 2 + 1 + 2 = 5$
\item $A \to C \to B \to E$: chi phí $= 2 + 1 + 3 = 6$
\end{itemize}
"""

lines[start_idx:end_idx+1] = [new_content]

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print("Done")
