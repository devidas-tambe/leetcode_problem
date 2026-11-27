paths = [
    ["B", "C"],
    ["D", "B"],
    ["C", "A"]
]

start = []

for i in paths:
    start.append(i[0])

for i in paths:
    if i[1] not in start:
        print(i[1])