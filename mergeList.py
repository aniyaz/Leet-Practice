#Question Link: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

def mergeList(nums1: [int], m: int, nums2: [int], n: int) -> None:
    x = m - n
    for num in nums2:
        nums1.insert(x, num)
        x += 1
    nums1 = sorted(nums1)
    print(nums1)
    return None

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = len(nums1)
    n = len(nums2)
    mergeList(nums1, m, nums2, n)
