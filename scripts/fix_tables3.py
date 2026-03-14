with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

# Insert captions after specific \end{tabular} or \end{longtable} lines
# We insert AFTER the \end{center} line that follows each table

insertions = []  # (line_number_0indexed, caption_text)

# Find each table end by looking for patterns
for i in range(len(lines)):
    line = lines[i].strip()
    
    # Master Theorem 3 cases - longtable near "Cho T(n) = aT(n/b)"
    if line == '\\end{longtable}' and i > 0:
        # Check context 30 lines back
        context = ''.join(lines[max(0,i-30):i])
        
        if 'aT(n/b)' in context and 'tab:master-theorem' not in ''.join(lines[max(0,i-5):i+5]):
            # Insert after the } on next line
            for j in range(i+1, min(i+3, len(lines))):
                if lines[j].strip() == '}':
                    insertions.append((j+1, '\\captionof{table}{Master Theorem -- Ba trường hợp}\\label{tab:master-theorem}\n'))
                    break
        
        if 'Merge Sort, Quick Sort' in context and 'tab:dp-vs-dc' not in ''.join(lines[max(0,i-5):i+5]):
            for j in range(i+1, min(i+3, len(lines))):
                if lines[j].strip() == '}':
                    insertions.append((j+1, '\\captionof{table}{So sánh Dynamic Programming và Divide \\& Conquer}\\label{tab:dp-vs-dc}\n'))
                    break
    
    if line == '\\end{tabular}' and i > 0:
        context = ''.join(lines[max(0,i-30):i])
        next3 = ''.join(lines[i+1:min(i+5, len(lines))])
        
        # Dijkstra edge table - contains "Cạnh" and "$w$"
        if 'Cạnh' in context and '$w$' in context and 'Dijkstra' in context and 'tab:dijkstra-edges' not in next3:
            for j in range(i+1, min(i+3, len(lines))):
                if '\\end{center}' in lines[j]:
                    insertions.append((j, '\\captionof{table}{Dijkstra -- Danh sách cạnh đồ thị mẫu}\\label{tab:dijkstra-edges}\n'))
                    break
        
        # Dijkstra trace - contains "ExtractMin"
        if 'ExtractMin' in context and 'tab:dijkstra-trace' not in next3:
            for j in range(i+1, min(i+3, len(lines))):
                if '\\end{center}' in lines[j]:
                    insertions.append((j, '\\captionof{table}{Dijkstra -- Bảng trace khoảng cách từng bước}\\label{tab:dijkstra-trace}\n'))
                    break
        
        # Floyd D^0 - contains "$D^{(0)}$" or "D^{(0)}"  
        if 'D^{(0)}' in context and 'tab:floyd-d0' not in next3:
            for j in range(i+1, min(i+3, len(lines))):
                if '\\end{center}' in lines[j]:
                    insertions.append((j, '\\captionof{table}{Floyd-Warshall -- Ma trận khoảng cách ban đầu $D^{(0)}$}\\label{tab:floyd-d0}\n'))
                    break
        
        # NP reduction table - contains "$L' \leq_p L$" or "reduction"
        if 'leq_p' in context and 'NP-Complete' in context and 'tab:np-reduction' not in next3:
            for j in range(i+1, min(i+3, len(lines))):
                if '\\end{center}' in lines[j]:
                    insertions.append((j, '\\captionof{table}{Ý nghĩa chiều Reduction trong chứng minh NP-Complete}\\label{tab:np-reduction}\n'))
                    break

# Sort insertions in reverse order to maintain line numbers
insertions.sort(key=lambda x: x[0], reverse=True)

for line_idx, caption in insertions:
    lines.insert(line_idx, caption)
    print(f"Inserted at L{line_idx+1}: {caption.strip()[:60]}...")

with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
    f.writelines(lines)

print(f"\nDone! Inserted {len(insertions)} captions")
