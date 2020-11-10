import numpy

def printSolution(board, N): 
	print("--------------------------------------")
	for i in range(N): 
		for j in range(N): 
			print(str(int(board[i][j])), end = " ") 
		print()
	print("--------------------------------------")

def isSafe(board, row, col, N): 

	for i in range(col): 
		if board[row][i] == 1: 
			return False

	for i, j in zip(range(row, -1, -1), 
					range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	for i, j in zip(range(row, N, 1), 
					range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

def solveNQUtil(board, col, N): 

	if col >= N: 
		return True

	for i in range(N):

		if isSafe(board, i, col, N): 

			board[i][col] = 1

			if solveNQUtil(board, col + 1, N) == True: 
				return True

			board[i][col] = 0

	return False

def createBoard(N):
	board = numpy.zeros(shape=(N, N))
	
	return board
		

def solveNQ(N): 

	board = createBoard(N)

	if solveNQUtil(board, 0, N) == False: 
		print ("Solution does not exist") 
		return False

	printSolution(board, N) 
	return True

n = input("Size of board: ")

solveNQ(int(n))
