from collections import Counter
import re

f = open('multiplayer.txt', 'r')
g1 = open('summary-multiplayer-rooms.txt', 'w')
g2 = open('summary-multiplayer-ids.txt', 'w')
g3 = open('summary-multiplayer-usernames.txt', 'w')

rooms = []
ids = []
usernames = []

for line in f:
    room = re.search(r'(?<="Connection in room \\u001b\[95m)(.*?)(?=\\u001b)', line).group()
    id = re.search(r'(?<=userId: \\u001b\[94m)(.*?)(?=\\u001b)', line).group()
    username = re.search(r'(?<=username: \\u001b\[94m)(.*?)(?=\\u001b)', line).group()

    rooms.append(room)
    ids.append(id)
    usernames.append(username)

room_counter = Counter(rooms)
g1.write('Rooms: # of connections\n')
g1.write(f'# of unique rooms: {len(room_counter)}\n')
g1.write('-----\n')
for key, value in room_counter.most_common():
    g1.write(f'{key:<50} {value}\n')

id_counter = Counter(ids)
g2.write('IDs: # of connections\n')
g2.write(f'# of unique IDs: {len(id_counter)}\n')
g2.write('-----\n')
for key, value in id_counter.most_common():
    g2.write(f'{key:<50} {value}\n')

username_counter = Counter(usernames)
g3.write('Usernames: # of connections\n')
g3.write(f'# of unique usernames: {len(username_counter)}\n')
g3.write('-----\n')
for key, value in username_counter.most_common():
    g3.write(f'{key:<50} {value}\n')
