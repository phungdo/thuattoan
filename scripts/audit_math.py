import re

with open('LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Audit 1: Check space complexity notation (should be O or \Theta consistently)
# Quick Sort space should be O(\lg n) average, worst case depends on implementation.
# In CLRS, naive randomized quicksort space is O(\lg n) if tail recursion is optimized, else O(n).
print("=== QUICK SORT SPACE ===")
qs_lines = [l for l in content.split('\n') if 'Quick Sort' in l and 'Space' in l]
for l in qs_lines[:3]: print(l)

# Audit 2: Check Master Theorem cases
print("\n=== MASTER THEOREM ===")
mt = content[content.find('Master Theorem --'):content.find('Ví dụ áp dụng')]
print(mt[:500])

# Audit 3: Check Dijkstra initialization and Relaxation
print("\n=== DIJKSTRA RELAX ===")
lines = content.split('\n')
for i, l in enumerate(lines):
    if 'Relax' in l or 'relax' in l.lower():
        print(f"L{i}: {l.strip()[:80]}")

# Audit 4: Check NP-Complete definitions
print("\n=== NP COMPLETE ===")
for i, l in enumerate(lines):
    if 'NP-Complete' in l or 'NP-Hard' in l:
        print(f"L{i}: {l.strip()[:80]}")

