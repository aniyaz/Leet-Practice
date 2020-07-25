#Question Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/


def findMaxConsecutiveOnes(nums: [int]) -> int:
        count = 0
        count1 = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > count1:
                    count1 = count
                else:
                    pass
                count = 0
        if count > count1:
            return count
        return count1

if __name__ == "__main__":
    arr = []
    n = int(input("Enter an Array: "))
    for i in range(n):
        num = int(input("Number: " + str(i) + ":- "))
        arr.append(num)
    print(arr)
    result = findMaxConsecutiveOnes(arr)
    print("Result: " + str(result))