H, P = list(map(int, input().split()))
D = 0

C1, C2 = 0, 0
while C1 <= C2:
    D += 1
    C1 = (D * H + 999) // 1000 * 5 + (60 * D * H * P) / 10**5
    C2 = (D * H + 7999) // 8000 * 60 + (11 * D * H * P) / 10**5
print(D)