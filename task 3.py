files_count = 3
file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
result_file = 'result_file.txt'

files = [file1, file2, file3]


file_lines = []
for filename in files:
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        file_lines.append((filename, len(lines), ''.join(lines)))
    file_lines.sort(key=lambda x: x[1])

merged_file = '\n'.join('{}\n{}\n{}'.format(line[0], line[1], line[2]) for line in file_lines)
with open(result_file, 'w', encoding='utf-8') as f:
    f.write(merged_file)

