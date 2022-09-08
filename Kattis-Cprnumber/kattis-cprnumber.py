CPR = input()
C = [4,3,2,7,6,5,4,3,2,1]
sum = 0
CPR = list(CPR.replace("-", ""))
for x in range(len(C)):
    sum += int(CPR[x])*int(C[x])
if (sum%11) == 0:
    print("1")
else:
    print("0")