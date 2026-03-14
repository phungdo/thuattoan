with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'r') as f:
    lines = f.readlines()

# Find the second occurrence of the solutions section
first_found = False
second_start = None
second_end = None
for i, line in enumerate(lines):
    if r'\section{Lời giải -- Tại sao?' in line:
        if first_found:
            second_start = i
        else:
            first_found = True

if second_start:
    # Find the \section{Phụ lục after second occurrence  
    for i in range(second_start + 1, len(lines)):
        if r'\section{Phụ lục' in lines[i]:
            second_end = i
            break
    
    if second_end:
        print(f"Removing duplicate: lines {second_start+1} to {second_end}")
        del lines[second_start:second_end]
        
        with open('/Users/Apple/Downloads/thuattoan/LECTURE_NOTES_ALGORITHMS.tex', 'w') as f:
            f.writelines(lines)
        print("Done")
    else:
        print("Could not find end of duplicate")
else:
    print("No duplicate found")
