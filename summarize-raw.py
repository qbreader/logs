from collections import Counter
import regex

f = open('api-packet.txt', 'r')
g = open('summary-packet.txt', 'w')
h = open('summary-ip.txt', 'w')

set_names = []
ips = []

for line in f:
    try:
        set_name = regex.findall(r'(?<=setName=).*?(?=&)', line)[0]
        set_name = set_name.replace('%20', ' ').replace('%22', '"').replace('%23', '#').replace('%27', "'")

        if len(set_name) == 0:
            continue

        set_names.append(set_name)
        ips.append(regex.findall(r'(?<=fwd=\\").*?(?=\\")', line)[0])
    except IndexError:
        print(line)

counter = Counter(set_names)
g.write('Set Name: # of packets requested\n')
g.write(f'# of unique sets: {len(counter)} (total {len(set_names)} packets)\n')
g.write('-----\n')
for key, value in counter.most_common():
	g.write(f'{key:<50} {value}\n')

counter = Counter(ips)
h.write('IP address: # of packets requested\n')
h.write(f'# of unique IPs: {len(counter)}\n')
h.write('-----\n')
for key, value in counter.most_common():
	h.write(f'{key:<20} {value}\n')
