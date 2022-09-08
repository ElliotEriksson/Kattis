n = int(input())
x = list(int(x) for x in input().split())
s = 1
for i in range(1, n):
    if x[i] > x[i-1]: s += 1
print(s)