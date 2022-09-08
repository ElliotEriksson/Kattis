num = int(input())
if num < 100:
    print("99")
else:
    num += 1.1
    print((round(num/100)*100)-1)
    