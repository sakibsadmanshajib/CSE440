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