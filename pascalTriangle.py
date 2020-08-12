#Question Link: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/

k = int(input("Enter the value for K: "))
pList = []
for i in range(1, k+2):
    c = 1
    for j in range(1, i+1):
        if i == k+1:
            pList.append(c)
        c = int(c * (i - j) / j)
print(pList)