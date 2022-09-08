used = []
for x in range(10):
    nr = int(input())
    if (nr%42) not in used:
        used.append(nr%42)
print(len(used))