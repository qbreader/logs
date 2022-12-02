from collections import Counter
import re

f = open('raw.log', 'r')
g1 = open('summary-queries.txt', 'w')

query_strings = []

for line in f:
    query_string = re.search(r'(?<=string: \\u001b\[96m).*?(?=\\u001b)', line).group()
    query_string = query_string.replace('\\\\', '\\')

    query_strings.append(query_string)

query_string_counter = Counter(query_strings)
g1.write('Query String: # of times queried\n')
g1.write(f'# of unique queries: {len(query_string_counter)}\n')
g1.write(f'# of total queries: {len(query_strings)}\n')
g1.write('-----\n')
for key, value in query_string_counter.most_common():
    g1.write(f'{key:<50} {value}\n')
