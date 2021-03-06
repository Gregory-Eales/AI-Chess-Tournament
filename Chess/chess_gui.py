import pygame
from pygame.locals import *
from chess import Chess
import time


class ChessGUI(object):
    def __init__(self, size, sample_board):

        self.sample_board = sample_board
        pygame.init()
        self.Chess = Chess()
        self.screenX = size
        self.screenY = size
        flags = FULLSCREEN | DOUBLEBUF
        #flags = DOUBLEBUF
        self.screen = pygame.display.set_mode((size, size), flags)
        self.screen.set_alpha(None)
        self.piece_paths = self.get_piece_paths()
        self.piece_images = self.load_images()
        self.piece_being_held = None
        self.holding_piece = False
        pygame.display.set_caption('Chess')
        self.play_gui()

    def draw_chess_board(self):
        self.screen.blit(self.chess_background, (0, 0))

    def draw_pieces(self, board):
        for i in range(8):
            for j in range(8):
                if board[j][i] != '.':
                    self.draw_piece(board[j][i], x=i, y=j)

    def draw_piece(self, symbol, x, y, held=False):

        if held == True:
            return self.screen.blit(self.piece_images[symbol], (x, y))

        else:
            self.screen.blit(self.piece_images[symbol], (x * int(self.screenX / 8), y * int(self.screenX / 8)))

    def load_images(self):
        self.darkSquare = pygame.image.load('chess_assets/square_graydark.png').convert_alpha()
        self.darkSquare = pygame.transform.scale(self.darkSquare, (int(self.screenX / 8), int(self.screenY / 8)))
        self.lightSquare = pygame.image.load('chess_assets/square_graylight.png').convert_alpha()
        self.lightSquare = pygame.transform.scale(self.lightSquare, (int(self.screenX / 8), int(self.screenY / 8)))
        self.chess_background = pygame.image.load('chess_assets/chess_background.png').convert_alpha()

        piece_images = {}
        for key in self.piece_paths:
            piece_images[key] = pygame.image.load(self.piece_paths[key]).convert_alpha()
            piece_images[key] = pygame.transform.scale(piece_images[key],
                                                       (int(self.screenX / 8), int(self.screenY / 8)))

        return piece_images

    def play_gui(self):
        clock = pygame.time.Clock()
        condition = True
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

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.act_on_piece(pos[0], pos[1])

                # Check for QUIT event; if QUIT, set running to false
                elif event.type == QUIT:
                    running = False

            if self.holding_piece:
                condition = True
                self.screen.blit(self.image_placehold, (0, 0))
                pos = pygame.mouse.get_pos()
                pygame.display.update(self.screen.blit(self.piece_images[self.piece_being_held],
                                                       (pos[0] - self.screenX / 16, pos[1] - self.screenX / 16)))
                clock.tick(1000)




            elif not self.holding_piece and condition:
                self.draw_chess_board()
                self.draw_pieces(self.sample_board)
                pygame.display.flip()
                condition = False

    def act_on_piece(self, x, y):
        self.Chess.board = self.sample_board
        sectorX = x / (self.screenX / 8)
        sectorY = y / (self.screenY / 8)
        for i in range(9):
            if sectorX < i:
                sectorX = int(i - 1)
                break

        for i in range(9):
            if sectorY < i:
                sectorY = int(i - 1)
                break

        if self.sample_board[sectorY][sectorX] == "." and not self.holding_piece:
            pass


        elif not self.holding_piece:
            self.picked_up_at = [sectorX, sectorY]
            self.piece_being_held = self.sample_board[sectorY][sectorX]
            self.sample_board[sectorY][sectorX] = "."
            self.holding_piece = True
            self.draw_chess_board()
            self.draw_pieces(self.sample_board)
            pygame.display.flip()
            pygame.image.save(self.screen, "image_placehold.jpeg")
            self.image_placehold = pygame.image.load("image_placehold.jpeg").convert()


        elif self.holding_piece:

            move = [self.piece_being_held, self.picked_up_at, [sectorX, sectorY]]

            if self.Chess.check_legal(move):
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
