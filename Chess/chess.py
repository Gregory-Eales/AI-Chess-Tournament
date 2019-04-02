

class Chess(object):

	def __init__(self):

		self.board = self.reset_board()
		self.turn = "white"

	# resets the board
	def reset_board(self):
		board = []
		white_pawn = ["P", "P", "P", "P", "P", "P", "P", "P"]
		black_pawn = ["p", "p", "p", "p", "p", "p", "p", "p"]
		white_back = ["R", "H", "B", "Q", "K", "B", "H", "R"]
		black_back = ["r", "h", "b", "q", "k", "b", "h", "r"]
		empty1 = [".", ".", ".", ".", ".", ".", ".", "."]
		empty2 = [".", ".", ".", ".", ".", ".", ".", "."]
		empty3 = [".", ".", ".", ".", ".", ".", ".", "."]
		empty4 = [".", ".", ".", ".", ".", ".", ".", "."]

		board.append(white_back)
		board.append(white_pawn)
		board.append(empty1)
		board.append(empty2)
		board.append(empty3)
		board.append(empty4)
		board.append(black_pawn)
		board.append(black_back)
		return board

	# prints the board state
	def print_board(self):
		print("-----------------------------------")
		for i in range(8):

			for j in range(8):
				if j == 0:
					print("| ", self.board[i][j], " ", end =" ")
				elif j == 7:
					print(self.board[i][j], " |" , i+1)
				else:
					print(self.board[i][j], " ", end =" ")

			if i!=7:
				print("|                                 |")

		print("-----------------------------------")

		print("   1   2   3   4   5   6   7   8")

	# resets the game
	def reset_game(self):
		self.turn = "white"
		self.board = self.reset_board()


	# runs the main game loop
	def play(self):

		# start with whos turn it is
			# get there move
			# check if its legal
			# make move
			# check if checkmate
			# change turn
		

		playing = True

		while playing:

			deciding_turn = True


			while deciding_turn:
				self.print_board()

				move = self.get_player_move()


				if self.check_legal(move):
					deciding_turn=False
					self.change_turn()
				else:
					print("Invalid Move, Try Again")

	# gets the player move irl
	def get_player_move(self):
		print("Its", self.turn, "to move")
		piece = input("which peice would you like to move: ")
		piece_pos = [int(piece[0])-1, int(piece[1])-1]
		piece_type = self.board[piece_pos[0]][piece_pos[1]]
		self.board[piece_pos[0]][piece_pos[1]] = "."
		new_pos = input("Where would you like to move: ")
		new_pos = [int(new_pos[0])-1, int(new_pos[1])-1]
		self.board[new_pos[0]][new_pos[1]] = piece_type
		return [piece_type, piece_pos, new_pos]
		


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
	def check_legal(self, move):
		piece_type, piece_pos, new_pos = move[0], move[1], move[2]
		print(piece_type, piece_pos, new_pos)

		if piece_type.lower() == "p":
			if piece_type.lower() == piece_type:
				print(new_pos[1] + 1, piece_pos[1])
				if piece_pos[1] == new_pos[1] + 1 and piece_pos[0] == new_pos[0]:
					return self.check_new_location(new_pos, "black")


			else:
				print(new_pos[1] - 1, piece_pos[1])
				if piece_pos[1] == new_pos[1] - 1 and piece_pos[0] == new_pos[0]:
					return self.check_new_location(new_pos, "white")


			if piece_type.lower() == piece_type:
				print(new_pos[1] + 2, piece_pos[1])
				if piece_pos[1] == new_pos[1] + 2 and piece_pos[0] == new_pos[0]:
					if piece_pos[1] == 8:
						return self.check_new_location(new_pos, "black")


			else:
				print(new_pos[1] - 2, piece_pos[1])
				if piece_pos[1] == new_pos[1] - 2 and piece_pos[0] == new_pos[0]:
					if piece_pos[1] == 1:
						return self.check_new_location(new_pos, "white")


		if piece_type.lower() == "r":
			if piece_type.lower() == piece_type:
				if piece_pos[0] == new_pos[0] or piece_pos[1] == new_pos[1]:
					return self.check_new_location(new_pos, "black")

			else:
				if piece_pos[0] == new_pos[0] or piece_pos[1] == new_pos[1]:
					return self.check_new_location(new_pos, "white")

		if piece_type.lower() == "h":
			if piece_type.lower() == piece_type:
				if piece_pos[0] == new_pos[0] + 2 or piece_pos[0] == new_pos[0] - 2:
					print("cond 1")
					if piece_pos[1] == new_pos[1] + 1 or piece_pos[1] == new_pos[1] - 1:
						print("cond 2")
						return self.check_new_location(new_pos, "black")

					
				if piece_pos[1] == new_pos[1] + 2 or piece_pos[1] == new_pos[1] - 2:
					print("cond 3")
					if piece_pos[0] == new_pos[0] + 1 or piece_pos[0] == new_pos[0] - 1:
						print("cond 4")
						return self.check_new_location(new_pos, "black")
			else:
				if piece_pos[0] == new_pos[0] + 2 or piece_pos[0] == new_pos[0] - 2:
					if piece_pos[1] == new_pos[1] + 1 or piece_pos[1] == new_pos[1] - 1:
						return self.check_new_location(new_pos, "white")

					
				if piece_pos[1] == new_pos[1] + 2 or piece_pos[1] == new_pos[1] - 2:
					if piece_pos[0] == new_pos[0] + 1 or piece_pos[0] == new_pos[0] - 1:
						return self.check_new_location(new_pos, "white")

		if piece_type.lower() == "b":
			if piece_type.lower() == piece_type:
				
				for i in range(8):

					if piece_pos[0] == new_pos[0] + i or piece_pos[0] == new_pos[0] - i:
						if piece_pos[1] == new_pos[1] + i or piece_pos[1] == new_pos[1] - i:
							return self.check_new_location(new_pos, "black")


			else:
				for i in range(8):

					if piece_pos[0] == new_pos[0] + i or piece_pos[0] == new_pos[0] - i:
						if piece_pos[1] == new_pos[1] + i or piece_pos[1] == new_pos[1] - i:
							return self.check_new_location(new_pos, "white")

		if piece_type.lower() == "k":
			if piece_type.lower() == piece_type:
				if piece_pos[0] == new_pos[0] + 1 or piece_pos[0] == new_pos[0] - 1 or piece_pos[0] == new_pos[0]:
					if piece_pos[1] == new_pos[1] + 1 or piece_pos[1] == new_pos[1] - 1 or piece_pos[1] == new_pos[1]:
						return self.check_new_location(new_pos, "black")

			else:
				if piece_pos[0] == new_pos[0] + 1 or piece_pos[0] == new_pos[0] - 1 or piece_pos[0] == new_pos[0]:
					if piece_pos[1] == new_pos[1] + 1 or piece_pos[1] == new_pos[1] - 1 or piece_pos[1] == new_pos[1]:
						return self.check_new_location(new_pos, "white")

		if piece_type.lower() == "q":
			if piece_type.lower() == piece_type:

				if piece_pos[0] == new_pos[0] or piece_pos[1] == new_pos[1]:
					return self.check_new_location(new_pos, "black")


				for i in range(8):
					if piece_pos[0] == new_pos[0] + i or piece_pos[0] == new_pos[0] - i:
						if piece_pos[1] == new_pos[1] + i or piece_pos[1] == new_pos[1] - i:
							return self.check_new_location(new_pos, "black")

			else:

				if piece_pos[0] == new_pos[0] or piece_pos[1] == new_pos[1]:
					return self.check_new_location(new_pos, "white")

				for i in range(8):

					if piece_pos[0] == new_pos[0] + i or piece_pos[0] == new_pos[0] - i:
						if piece_pos[1] == new_pos[1] + i or piece_pos[1] == new_pos[1] - i:
							return self.check_new_location(new_pos, "white")
				

		if piece_type.lower() == ".":
			pass

		return False

	def check_new_location(self, loc, color):
		new_pos_type = self.board[loc[1]][loc[0]]
		new_color = None




		if new_pos_type.lower() == new_pos_type and new_pos_type != ".":
			new_color = "black"

		elif new_pos_type != ".":
			new_color = "white"

		if color != new_color:
			return True

		else:
			print("Failed")
			print(color, new_color, new_pos_type)
			return False
		


	# check if anyones in check
	def check_if_check(self):
		pass

	# moves piece to location
	def move_peice(self):
		pass

	def change_turn(self):
		if self.turn == "white":
			self.turn = "black"
		if self.turn == "black":
			self.turn = "white"

if __name__ == '__main__':
	chss = Chess()
	chss.play()

