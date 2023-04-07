from collections import Counter
from urllib.parse import unquote

import regex

f = open('raw.log', 'r', encoding='utf-8-sig')
g1 = open('summary-queries.txt', 'w')
g2 = open('summary-ip.txt', 'w')

query_strings = []
ips = []
stats = {
    'randomize': 0,
    'ignoreDiacritics': 0,
    'regex': 0,
}

for line in f:
    line = line.strip()

    if line in ['"message"', '']:
        continue

    try:
        query_string = regex.findall(r'(?<=queryString=).*?(?=&)', line)[0]
        query_string = unquote(query_string)
        query_strings.append(query_string)
    except:
        query_strings.append('')

    try:
        ip = regex.findall(r'(?<=fwd=[\\"]").*?(?=[\\"]")', line)[0]
        ips.append(ip)

        for stat in stats:
            if f'{stat}=true&' in line:
                stats[stat] += 1
    except:
        print(line)


query_string_counter = Counter(query_strings)
g1.write('Query String: # of times queried\n')
g1.write(f'# of unique queries: {len(query_string_counter)}\n')
g1.write(f'# of total queries: {len(query_strings)}\n')
g1.write('-----\n')
for key, value in query_string_counter.most_common():
    g1.write(f'{key:<50} {value}\n')


counter = Counter(ips)
g2.write('IP address: # of packets requested\n')
g2.write(f'# of unique IPs: {len(counter)}\n')
g2.write('-----\n')
for key, value in counter.most_common():
    g2.write(f'{key:<20} {value}\n')

print(f'# of queries: {len(query_strings)}')
print(stats)
