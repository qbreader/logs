from collections import Counter
from urllib.parse import parse_qs, urlparse
import regex

f = open("raw.log", "r", encoding="utf-8-sig")

ips = []

tossup_count = 0
bonus_count = 0

parameters = {
    "difficulties": [],
    "categories": [],
    "subcategories": [],
}

for line in f:
    line = line.strip()

    if line in ['"message"', ""]:
        continue

    try:
        if "status=404" in line:
            continue

        ip = regex.search(r'(?<=fwd=[\\"]").*?(?=[\\"]")', line).group(0)
        ips.append(ip)

        path = regex.search(r'(?<=path="")[^"]*(?="")', line).group(0)
        query = urlparse(path).query
        qs = parse_qs(query)

        for parameter in parameters:
            if parameter in qs:
                parameters[parameter] += qs[parameter][0].split(",")

        if "number" in qs:
            number = int(qs["number"][0])
        else:
            number = 1

        if "random-tossup" in path:
            tossup_count += number
        elif "random-bonus" in path:
            bonus_count += number
    except IndexError:
        print(line)

print("Tossups:", tossup_count)
print("Bonuses:", bonus_count)


max_parameter_length = max([len(parameter) for parameter in parameters])

for parameter in parameters:
    with open(f"summary-{parameter}.txt", "w") as g:
        counter = Counter(parameters[parameter])
        max_length = max([len(key) for key in counter])
        g.write(f"{parameter}: # of times requested\n")
        g.write("-----\n")
        for key, value in counter.most_common():
            g.write(f"{key:<{max_length + 5}} {value}\n")


with open("summary-ip.txt", "w") as g:
    counter = Counter(ips)
    g.write("IP address: # of requests\n")
    g.write(f"# of unique IPs: {len(counter)}\n")
    g.write("-----\n")
    for key, value in counter.most_common():
        g.write(f"{key:<50} {value}\n")
