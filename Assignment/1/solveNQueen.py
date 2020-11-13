"""
1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column. 
   Do following for every tried row.
    a) If the queen can be placed safely in this row 
       then mark this [row, column] as part of the 
       solution and recursively check if placing
       queen here leads to a solution.
    b) If placing the queen in [row, column] leads to
       a solution then return true.
    c) If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to 
       step (a) to try other rows.
3) If all rows have been tried and nothing worked,
   return false to trigger backtracking.
"""

import numpy

solN = 0

def printBoard(board):
	global solN
	solN = solN + 1
	print("--------------------------------------\nPossibility #",solN)
	for i in range(len(board)): 
		for j in range(len(board)):
			if board[i][j] == 1:
				print("Q", end = " ")
			else:
				print("x", end = " ") 
		print()
	print("--------------------------------------")

def isSafe(board, row, col): 

	for i in range(col): 
		if board[row][i] == 1: 
			return False

	for i, j in zip(range(row, -1, -1), 
					range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	for i, j in zip(range(row, len(board), 1), 
					range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

def placeQueen(board, col): 

	if col >= len(board): 
		printBoard(board)
		return True

	for i in range(len(board)):

		isValid = False
		for i in range(len(board)):
			if isSafe(board, i, col): 

				board[i][col] = 1

				isValid = placeQueen(board, col + 1) or isValid

				board[i][col] = 0
		return False

def createBoard(N):	
	return numpy.zeros(shape=(N, N))
		
def solveNQueen(N): 

	board = createBoard(N)

	if placeQueen(board, 0) == False: 
		print("Can't find any solution.") 
		return board

	return board

def main():
	n = input("Size of board: ")
	solveNQueen(int(n))

if __name__ == '__main__':
    main()