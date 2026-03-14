import re

with open('LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Audit 5: Master Theorem exact math notation
print("=== MASTER THEOREM EXACT ===")
mt = content[content.find('Master Theorem --'):content.find('Ví dụ áp dụng')]
print(mt)

# Audit 6: Loop Invariant for Insertion Sort
print("\n=== INSERTION SORT LI ===")
li = content[content.find('Loop Invariant (Insertion Sort)'):content.find('Phân tích Complexity (CLRS')]
if not li:
    li = content[content.find('Chứng minh đúng đắn (Loop Invariant'):content.find('Phân tích Complexity (CLRS')]
print(li[:600])

