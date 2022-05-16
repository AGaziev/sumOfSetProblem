inpSet = [-20, -4, 6, 1, 18, 5, -3, 3, -1]
setWithSum0 = [inpSet[0]]
sum = inpSet[0]
size = len(inpSet)
for i in range(1, size):
    if (abs(sum + inpSet[i]) < abs(sum)):
        sum += inpSet[i]
        setWithSum0.append(inpSet[i])
if sum==0:
    for i,num in enumerate(setWithSum0):
        print(num, end=' ')
else:
    print('no sets with greedy')