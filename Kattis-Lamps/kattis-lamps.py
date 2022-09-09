H, P = list(map(int, input().split()))
Days = 0

Cost_bulb, Cost_led = 0, 0
while Cost_bulb <= Cost_led:
    Days += 1
    Cost_bulb = (Days * H + 999) // 1000 * 5 + (60 * Days * H * P) / 10**5
    Cost_led = (Days * H + 7999) // 8000 * 60 + (11 * Days * H * P) / 10**5
print(Days)