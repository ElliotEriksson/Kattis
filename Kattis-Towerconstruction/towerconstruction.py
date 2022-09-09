amount = int(input())
parts = list(int(parts) for parts in input().split())
towers = 1
for i in range(1, amount):
    if parts[i] > parts[i-1]: towers += 1
print(towers)