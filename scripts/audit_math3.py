import re

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Audit 7: Matrix Chain Multiplication DP formula
print("=== MATRIX CHAIN DP ===")
mc_idx = content.find('Matrix Chain Multiplication')
if mc_idx != -1:
    end_idx = content.find('subsection', mc_idx + 10)
    print(content[mc_idx:mc_idx+800])

# Audit 8: Floyd-Warshall DP recursive formula
print("\n=== FLOYD-WARSHALL DP ===")
fw_idx = content.find('D^{(k)}[i][j] =')
if fw_idx != -1:
    print(content[max(0, fw_idx-100):fw_idx+200])

# Audit 9: Check \log notation (should be \lg for base 2 in CS, or \ln, \log)
print("\n=== LOG NOTATION COUNT ===")
print("Count of \\lg:", content.count('\\lg'))
print("Count of \\log_2:", content.count('\\log_2'))
print("Count of \\log (without base):", len(re.findall(r'\\log[^_]', content)))
