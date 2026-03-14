# Inline Union-Find (no external dependency)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def issame(self, a, b):
        return self.find(a) == self.find(b)
    def unite(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]: a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]: self.rank[a] += 1

def make_graph():
    return {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }

def conv_char(c): return ord(c) - 65

def kruskals(G):
    total_cost = 0; MST = []
    edges = []
    for _, value in G.items():
        edges.extend(value)
    num_nodes = len(G)
    edges = sorted(edges)
    uf = UnionFind(num_nodes)
    print("=== KRUSKAL TRACE ===")
    for edge in edges:
        cost, n1, n2 = edge[0], edge[1], edge[2]
        if not uf.issame(conv_char(n1), conv_char(n2)):
            total_cost += cost
            uf.unite(conv_char(n1), conv_char(n2))
            MST.append((n1, n2, cost))
            print(f"  ACCEPT: {n1}{n2} (w={cost})")
        else:
            print(f"  REJECT: {n1}{n2} (w={cost}) -- cycle")
    return MST, total_cost

G = make_graph()
MST, total_cost = kruskals(G)
print(f'\nMST edges: {MST}')
print(f'Total cost: {total_cost}')
