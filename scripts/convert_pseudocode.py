import re

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Map of pseudocode names based on content first line
name_map = {
    'Fib(n):': 'Fibonacci -- Đệ quy',
    'Fib2(n):': 'Fibonacci -- DP Bottom-up',
    'Fib3(n):': 'Fibonacci -- DP tối ưu space',
    'InsertionSort(A, n):': 'Insertion Sort',
    'MergeSort(A, p, r):': 'Merge Sort',
    'QuickSort(A, p, r):': 'Quick Sort',
    'RandomizedPartition(A, p, r):': 'Randomized Partition',
    'MaxHeapify(A, i, n):': 'Heap Sort (MaxHeapify + BuildMaxHeap + HeapSort)',
    'Muc 0:': 'Cây đệ quy (Recursion Tree)',
    'Vi du: V = {a,b,c,d,e}': 'Danh sách kề (Adjacency List)',
    'A[i][j] = 1 neu (i,j) in E': 'Ma trận kề (Adjacency Matrix)',
    'Input: Tap S, dieu kien (1)': 'Greedy Framework',
    'Kruskal(G, w):': 'Kruskal\'s Algorithm',
    'Prim(G, w, s):': 'Prim\'s Algorithm',
    'Relax(u, v, w):': 'Relaxation',
    'Dijkstra(G, w, s):': 'Dijkstra\'s Algorithm',
    'Pascal1(n, k):': 'Pascal Triangle -- DP (O(nk) space)',
    'Pascal2(n, k):': 'Pascal Triangle -- DP tối ưu (O(k) space)',
    'Floyd-Warshall(W):': 'Floyd-Warshall',
    'MatrixChainOrder(p):': 'Matrix Chain Multiplication',
    '1. Viet T(n) = aT(n/b)': 'Template Master Theorem',
    '1. d[s]=0, d[v]=INF': 'Template Dijkstra',
    'Kruskal: Sap canh tang dan': 'Template MST',
    '1. Chung minh in NP': 'Template chứng minh NP-Complete',
}

def get_name(block_content):
    first_line = block_content.strip().split('\n')[0].strip()
    for key, name in name_map.items():
        if first_line.startswith(key):
            return name
    return 'Algorithm'

# Find all verbatim blocks and replace
counter = [0]

def replace_verbatim(match):
    counter[0] += 1
    block = match.group(1)
    name = get_name(block)
    return (
        f'\\begin{{tcolorbox}}[colback=gray!8, colframe=gray!50, '
        f'boxrule=0.5pt, arc=2pt,\n'
        f'  left=6pt, right=6pt, top=4pt, bottom=4pt,\n'
        f'  title={{\\small\\textbf{{Pseudocode {counter[0]}: {name}}}}}]\n'
        f'\\begin{{verbatim}}\n'
        f'{block}'
        f'\\end{{verbatim}}\n'
        f'\\end{{tcolorbox}}'
    )

content = re.sub(
    r'\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}',
    replace_verbatim,
    content,
    flags=re.DOTALL
)

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.write(content)

print(f"Converted {counter[0]} verbatim blocks")
