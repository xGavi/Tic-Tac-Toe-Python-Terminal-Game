class Cell:
	def __init__(self, x, y, state = '-'):
		self.x = x
		self.y = y
		self.state = state

	def __repr__(self):
		if self.state == '-':
			return ' '
		return self.state


class Board:
	def __init__(self):
		self.boardDict = {(cell, cell.state) for cell in cells}
		self.boardRows = [[], [], []]
		self.boardColumns = [[], [], []]
		self.boardDiagonals = [[], []]
		self.winC = []
			
	def __repr__(self):
		board =f'''
 _____ _                 _____                     _____          
|_   _(_)               |_   _|                   |_   _|         
  | |  _  ___   ______    | | __ _  ___   ______    | | ___   ___ 
  | | | |/ __| |______|   | |/ _` |/ __| |______|   | |/ _ \\ / _ \\
  | | | | (__             | | (_| | (__             | | (_) |  __/
  \\_/ |_|\\___|            \\_/\\__,_|\___|            \\_/\\___/ \\___|

		          a     b     c
		             |     |     
		       1  {c0}  |  {c1}  |  {c2}  
		        _____|_____|_____
		             |     |     
		       2  {c3}  |  {c4}  |  {c5}  
		        _____|_____|_____
		             |     |     
		       3  {c6}  |  {c7}  |  {c8}  
		             |     |     
          '''
		return board

	def genRows(self):
		count = 0
		for cell in cells:
			if count < 3:
				(self.boardRows[0]).append(cell.state)
				count += 1
			elif count < 6:
				(self.boardRows[1]).append(cell.state)
				count += 1
			elif count < 9:
				(self.boardRows[2]).append(cell.state)
				count += 1
		return self.boardRows

	def genColumns(self):
		count = 1
		for cell in cells:
			if count % 3 == 1:
				(self.boardColumns[0]).append(cell.state)
				count += 1
			elif count % 3 == 2:
				(self.boardColumns[1]).append(cell.state)
				count += 1
			elif count % 3 == 0:
				(self.boardColumns[2]).append(cell.state)
				count += 1
		return self.boardColumns

	def genDiagonals(self):
		count = 1
		for cell in cells:
			if count == 1 or count == 9:
				(self.boardDiagonals[0]).append(cell.state)
				count += 1
			elif count == 3 or count == 7:
				(self.boardDiagonals[1]).append(cell.state)
				count += 1
			elif count == 5:
				(self.boardDiagonals[0]).append(cell.state)
				(self.boardDiagonals[1]).append(cell.state)
				count += 1
			else:
				count += 1
		return self.boardDiagonals

	def winConditions(self):
		for triplet in self.genRows():
			self.winC.append(triplet)
		for triplet in self.genColumns():
			self.winC.append(triplet)
		for triplet in self.genDiagonals():
			self.winC.append(triplet)
		return self.winC

	def checkWin(self):
		winO = ['O', 'O', 'O']
		winX = ['X', 'X', 'X']
		for triplet in self.winConditions():
			if triplet == winO:
				return 'Player O wins!'
			elif triplet == winX:
				return 'Player X wins!'
			else:
				return ''

xCount = 1
yCount = 1
cells = []
for i in range(9):
	globals()[f'c{i}'] = Cell(xCount, yCount)
	cells.append(globals()[f'c{i}'])
	xCount += 1
	if xCount == 3:
		xCount = 1
		yCount += 1