import pygame
from pygame.locals import *
from chess import Chess
import time


class ChessGUI(object):

	def __init__(self, size, sample_board):

		self.sample_board = sample_board
		pygame.init()
		self.screenX = size
		self.screenY = size
		self.screen = pygame.display.set_mode((size, size))
		self.piece_paths = self.get_piece_paths()
		self.piece_images = self.load_images()
		self.piece_being_held = None
		self.holding_piece = False
		pygame.display.set_caption('Chess')
		self.play_gui()

		

	def draw_chess_board(self):

		for i in range(8):
			for j in range(8):

				if i%2 == 0:
					if j%2 == 0:
						self.screen.blit(self.darkSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))

					else:
						self.screen.blit(self.lightSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))

				elif i%2 != 0:
					if j%2 != 0:
						self.screen.blit(self.darkSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))

					else:
						self.screen.blit(self.lightSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))



	def draw_pieces(self, board):
		for i in range(8):
			for j in range(8):
				if board[j][i] != '.':
					self.draw_piece(board[j][i], x=i, y=j)

	def draw_piece(self, symbol, x, y, held=False):

		if held == True:
			self.screen.blit(self.piece_images[symbol], (x, y))
			return 0

		self.screen.blit(self.piece_images[symbol], (x*int(self.screenX/8), y*int(self.screenX/8)))

	def load_images(self):
		self.darkSquare = pygame.image.load('chess_assets/square_graydark.png')
		self.darkSquare = pygame.transform.scale(self.darkSquare, (int(self.screenX/8), int(self.screenY/8)))
		self.lightSquare = pygame.image.load('chess_assets/square_graylight.png')
		self.lightSquare = pygame.transform.scale(self.lightSquare, (int(self.screenX/8), int(self.screenY/8)))

		piece_images = {}
		for key in self.piece_paths:
			piece_images[key] = pygame.image.load(self.piece_paths[key])
			piece_images[key] = pygame.transform.scale(piece_images[key], (int(self.screenX/8), int(self.screenY/8)))

		return piece_images

	def play_gui(self):
		# Variable to keep our main loop running
		running = True
		# Our main loop!
		while running:
		    # for loop through the event queue
		    pygame.event.wait()
		    for event in pygame.event.get():
		        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
		        if event.type == KEYDOWN:
		            # If the Esc key has been pressed set running to false to exit the main loop
		            if event.key == K_ESCAPE:
		                running = False

		        if event.type == pygame.MOUSEBUTTONUP:
		        	pos = pygame.mouse.get_pos()
		        	self.act_on_piece(pos[0], pos[1])
		        # Check for QUIT event; if QUIT, set running to false
		        elif event.type == QUIT:
		            running = False

		    self.draw_chess_board()
		    self.draw_pieces(self.sample_board)
		    if self.holding_piece:
		    	pos = pygame.mouse.get_pos()
		    	pos = (pos[0] - self.screenX/16, pos[1] - self.screenX/16)
		    	self.draw_piece(self.piece_being_held, pos[0], pos[1], held=True)
	
		    pygame.display.flip()


	def act_on_piece(self, x, y):
		sectorX = x/(self.screenX/8)
		sectorY = y/(self.screenY/8)
		for i in range(9):
			if sectorX < i:
				sectorX = int(i - 1)
				break

		for i in range(9):
			if sectorY < i:
				sectorY = int(i-1)
				break


		if self.sample_board[sectorY][sectorX] == "." and not self.holding_piece :
			pass


		elif not self.holding_piece:
			print("You clicked")
			self.piece_being_held = self.sample_board[sectorY][sectorX]
			self.sample_board[sectorY][sectorX] = "."
			self.holding_piece = True

		elif self.holding_piece:
			self.sample_board[sectorY][sectorX] = self.piece_being_held
			self.piece_being_held = None
			self.holding_piece = False

		
	def get_piece_paths(self):
		piece_paths = {}
		piece_paths["b"] = "chess_assets/b_bishop.png"
		piece_paths["B"] = "chess_assets/w_bishop.png"
		piece_paths["r"] = "chess_assets/b_rook.png"
		piece_paths["R"] = "chess_assets/w_rook.png"
		piece_paths["h"] = "chess_assets/b_knight.png"
		piece_paths["H"] = "chess_assets/w_knight.png"
		piece_paths["q"] = "chess_assets/b_queen.png"
		piece_paths["Q"] = "chess_assets/w_queen.png"
		piece_paths["p"] = "chess_assets/b_pawn.png"
		piece_paths["P"] = "chess_assets/w_pawn.png"
		piece_paths["k"] = "chess_assets/b_king.png"
		piece_paths["K"] = "chess_assets/w_king.png"
		return piece_paths



chss = Chess()
chess_gui = ChessGUI(720, chss.board)

