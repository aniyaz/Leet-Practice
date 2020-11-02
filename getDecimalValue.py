#Question Link: https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3516/

def getDecimalValue(head):
    if len(head) < 1:
        return
    j = len(head) - 1
    result = 0
    for i in range(len(head)):
        if head[i] == 1:
            result += 2 ** j
        j -= 1
    return result

if __name__ == "__main__":
    l = [1,0,1]
    print(getDecimalValue(l))