#Question Link: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

def sortedSquares(A: [int]) -> [int]:
    result = []
    for num in A:
        result.append(num * num)
    return sorted(result)

if __name__ == "__main__":
    arr = []
    n = int(input("Enter an Array: "))
    for i in range(n):
        num = int(input("Number: " + str(i) + ":- "))
        arr.append(num)
    print(arr)
    result = sortedSquares(arr)
    print("Resultant List: \n", result)