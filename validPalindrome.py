#Question Link: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/

def isPalindrome(s: str) -> bool:
    s1 = ''
    for char in s:
        if(char.isalnum()):
            s1 += char
    if(len(s1)%2 == 0):
        return (s1[:len(s1)//2]).lower() == ((s1[len(s1)//2 : len(s1)])[::-1]).lower()
        
    else:
        return (s1[:len(s1)//2+1]).lower() == ((s1[len(s1)//2 : len(s1)])[::-1]).lower()
    
if __name__ == "__main__":
    s = input("Enter string: ")
    print(isPalindrome(s))
    