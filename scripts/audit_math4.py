import re

with open('LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Find the Matrix Chain Multiplication formula
print("=== MATRIX CHAIN MULTIPLICATION FORMULA ===")
mc_idx = content.find('m[i,j] =')
if mc_idx != -1:
    print(content[max(0, mc_idx-100):mc_idx+300])

# Find \log without base
print("\n=== LOG WITHOUT BASE ===")
lines = content.split('\n')
for i, l in enumerate(lines):
    if re.search(r'\\log[^_]', l) and 'log_b a' not in l:
        print(f"L{i}: {l.strip()}")
