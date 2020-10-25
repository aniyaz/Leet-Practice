#Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/
#TO be continued
import numpy as np

def isValidSudoku(board):
    sample = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for small in board:
        print("Nothing")

def row_check(board):
    flag = True
    for row in board:
        for element in row:
            if element == ".":
                continue
            else:
                if row.count(element) != 1:
                    flag = False
                    return flag
                else:
                    continue
    return flag

def transpose(board):
    result = []
    row = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            row.append(board[j][i])
        result.append(row)
        row = []
    return result

def col_check(board):
    return row_check(transpose(board))
    
def cube_check(board):
    i = j = 0
    for eachRow in board:
        print(eachRow[i+0 : j+3])
        i += 1
        j += 1


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

print(col_check(board))
print(row_check(board))
cube_check(board)