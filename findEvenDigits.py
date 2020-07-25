#Question Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/


def findNumbers(nums: [int]) -> int:
    digits = 0
    for num in nums:
        if len(str(num))%2 == 0:
            digits += 1
    return digits


if __name__ == "__main__":
    arr = []
    n = int(input("Enter an Array: "))
    for i in range(n):
        num = int(input("Number: " + str(i) + ":- "))
        arr.append(num)
    print(arr)
    result = findNumbers(arr)
    print("Result: " + str(result))