import re

with open('LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# MCM formula usually involves m[i,j] = min_{i<=k<j} (m[i,k] + m[k+1,j] + p_{i-1}p_k p_j)
m_lines = [l for l in content.split('\n') if 'm[i,j]' in l or 'm[i][j]' in l]
for l in m_lines:
    print(l.strip()[:100])
