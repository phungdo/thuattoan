import re

with open('LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    content = f.read()

# Extract the pseudocode block and the corresponding complexity table for each sort
sorts = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']

for s in sorts:
    print(f"\n==================== {s.upper()} ====================")
    
    # Simple regex to find the pseudocode and the table following it
    # We look for \begin{verbatim} ... \end{verbatim} near "Pseudocode X: [Sort Name]"
    match = re.search(r'Pseudocode \d+[a-z]?: ' + s.replace(" (CLRS 8.2)", "").replace(" (MaxHeapify + BuildMaxHeap + HeapSort)", "") + r'.*?\\begin\{verbatim\}(.*?)\\end\{verbatim\}.*?Phân tích Complexity.*?\\begin\{tabular\}(.*?)\\end\{tabular\}', content, re.DOTALL | re.IGNORECASE)
    
    if match:
        print("PSEUDOCODE:")
        print(match.group(1).strip())
        print("\nCOMPLEXITY TABLE:")
        print(match.group(2).strip())
    else:
        # Fallback if the regex is too strict
        idx = content.find(f'Pseudocode')
        while idx != -1:
            line_end = content.find(']', idx)
            title = content[idx:line_end]
            if s.split()[0] in title:
                print(f"FOUND TITLE: {title}")
                verb_start = content.find('\\begin{verbatim}', line_end)
                verb_end = content.find('\\end{verbatim}', verb_start)
                print("PSEUDOCODE:")
                print(content[verb_start+16:verb_end].strip())
                
                table_start = content.find('Phân tích Complexity', verb_end)
                if table_start != -1 and table_start - verb_end < 500:
                    tab_start = content.find('\\begin{tabular}', table_start)
                    tab_end = content.find('\\end{tabular}', tab_start)
                    print("\nCOMPLEXITY TABLE:")
                    print(content[tab_start+15:tab_end].strip())
                break
            idx = content.find('Pseudocode', idx + 10)

