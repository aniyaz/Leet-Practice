#Link: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492/

def buddyStrings(A, B) -> bool:
    A = list(A)
    B = list(B)
       
    alphaber_count = {}
    
    if len(A) != len(B):
        return False
    
    different_index = []
    for i in range(len(A)):
        if A[i] in alphaber_count:
            alphaber_count[A[i]] += 1
        else:
            alphaber_count[A[i]] = 1
            
        if A[i] != B[i]:
            different_index.append(i)
            
    # print(alphaber_count)
    if len(different_index) == 0:
        for alph in alphaber_count.keys():
            if alphaber_count[alph] >= 2:
                return True
        return False
    if len(different_index) != 2:
        return False
    
    A[different_index[0]], A[different_index[1]] = A[different_index[1]], A[different_index[0]]
    if A == B:
        return True
    
    return False

if __name__ == "__main__":
    A = input("Enter A: ")
    B = input("Enter B: ")
    print(buddyStrings(A, B))