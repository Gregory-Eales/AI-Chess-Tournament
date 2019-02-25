

class Chess(object):

	def __init__(self):

		self.board = self.reset_board()

	# resets the board
	def reset_board(self):
		board = []
		white_pawn = ["P", "P", "P", "P", "P", "P", "P", "P"]
		black_pawn = ["p", "p", "p", "p", "p", "p", "p", "p"]
		white_back = ["R", "H", "B", "Q", "K", "B", "H", "R"]
		black_back = ["r", "h", "b", "q", "k", "b", "h", "r"]
		empty = [".", ".", ".", ".", ".", ".", ".", "."]

		board.append(white_back)
		board.append(white_pawn)
		for i in range(4):
			board.append(empty)
		board.append(black_pawn)
		board.append(black_back)
		return board


	def print_board(self):
		print("-------------------------------------")
		for i in range(8):

			for j in range(8):
				if j == 0:
					print("|", self.board[i][j], " ", end =" ")
				if j == 7:
					print(self.board[i][j], "|")
				else:
					print(self.board[i][j], " ", end =" ")

			if i!=7:
				print("|                                   |")

		print("-------------------------------------")

	# runs the main game loop
	def play(self):
		pass

	# returns board state
	def get_board(self):
		pass

	# returns whos turn
	def get_turn(self):
		pass

	# gets all legal moves
	def get_legal_moves(self):
		pass

	# check if move is legal
	def check_legal(self):
		pass

	# check if anyones in check
	def check_if_check(self):
		pass

	# moves piece to location
	def move_peice(self):
		pass



chss = Chess()
chss.print_board()