#Link: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3512/

def maxDistanceToClosest(seats):
    reserved = [i for i, x in enumerate(seats) if x == 1]
    if len(reserved) == 1:
        return len(seats) - (reserved[0] + 1)
    print(reserved)


if __name__ == "__main__":
    seats = [0,1]

    maxDistanceToClosest(seats)
