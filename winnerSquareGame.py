#Question Link: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3507/
#Cornercase for n=8 doesn't satisfy.
import math

def winnerSquareGame(n):
    move = True
    while n != 0:
        n = n - maxSquare(n)
        if n == 0:
            return move
        else:
            move = toggle(move)

def toggle(cond):
    if cond:
        return False
    else:
        return True

def maxSquare(n):
    result = math.isqrt(n)
    return result * result

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print(winnerSquareGame(n))