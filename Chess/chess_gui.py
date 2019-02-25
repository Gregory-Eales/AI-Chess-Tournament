import pygame
from pygame.locals import *


class ChessGUI(object):

	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption('Chess')
		self.play_gui()



	def chess_board(self, x, y):
		pass

	


	def play_gui(self):
		# Variable to keep our main loop running
		running = True

		# Our main loop!
		while running:
		    # for loop through the event queue
		    for event in pygame.event.get():
		        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
		        if event.type == KEYDOWN:
		            # If the Esc key has been pressed set running to false to exit the main loop
		            if event.key == K_ESCAPE:
		                running = False
		        # Check for QUIT event; if QUIT, set running to false
		        elif event.type == QUIT:
		            running = False

chess_gui = ChessGUI()



