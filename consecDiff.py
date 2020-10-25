#Question Link: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/

N = int(input('Enter value of N: '))
K = int(input('Enter value of K: '))

minNum = pow(10, N-1)
maxNum = pow(10, N) - 1
tryNum = minNum
result = []
flag = False
while tryNum <= maxNum:
    strNum = str(tryNum)
    if len(strNum) < 2:
        if K == 0:
            for i in range(10):
                result.append(i)
        else:
            result = []
        break
    else:
        for i in range(len(strNum)-1):
            chk = abs(int(strNum[i]) - int(strNum[i+1]))
            if chk == K:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            result.append(tryNum)
        tryNum += 1
print(result)