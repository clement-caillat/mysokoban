import pygame
import pickle

class Editor:
    def __init__(self):
        self.board = []
        self.RUNNING = True
        self.screen = None
        self.grid_size = 10
        self.map_size = (800, 800)
        self.tile_size = self.map_size[0] // self.grid_size
        self.sprites = []
        self.cursor = 0
        self.player = 0
        self.crates = 0
        self.points = 0

    def load(self):
        board = open('./boards/virgin_board.txt', 'rb')
        self.board = pickle.load(board)
        ground = pygame.image.load('./PNG/ground.png')
        ground = pygame.transform.scale(ground, (self.tile_size, self.tile_size))
        wall = pygame.image.load('./PNG/wall.png')
        wall = pygame.transform.scale(wall, (self.tile_size, self.tile_size))
        crate = pygame.image.load('./PNG/crate.png')
        crate = pygame.transform.scale(crate, (self.tile_size, self.tile_size))
        point = pygame.image.load('./PNG/point.png')
        point = pygame.transform.scale(point, (self.tile_size, self.tile_size))
        player = pygame.image.load('./PNG/player_front.png')
        player = pygame.transform.scale(player, (self.tile_size, self.tile_size))
        save = pygame.image.load('./PNG/save.png')
        save = pygame.transform.scale(save, (self.tile_size, self.tile_size))
        self.sprites = [
            ground,
            wall,
            crate,
            point,
            player,
            save
        ]



    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('My Sokoban map editor')
        self.load()
        pygame.display.set_icon(self.sprites[1])
        self.draw_board()
        while self.RUNNING:
            pygame.display.flip()
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    x = event.pos[0]
                    y = event.pos[1]
                    x = x // (80 + 1)
                    y = y // (80 + 1)

                    print("x:{} y:{}".format(x, y))

                    if x == 13 and y == 0 or x == 14 and y == 0:
                        self.cursor = 0
                    elif x == 13 and y == 2 or x == 14 and y == 2:
                        self.cursor = 1
                    elif x == 13 and y == 3 or x == 14 and y == 3:
                        self.cursor = 2
                    elif x == 13 and y == 4 or x == 14 and y == 4:
                        self.cursor = 3
                    elif x == 13 and y == 5 or x == 14 and y == 5:
                        self.cursor = 4
                    elif x == 13 and y == 8 or x == 14 and y == 8:
                        if self.player == 1:
                            if self.crates == self.points:
                                name = input("Nom du fichier : ")
                                with open('boards/{}.txt'.format(name), 'wb') as fp:
                                    pickle.dump(self.board, fp)
                                    print("Saved")
                                    self.RUNNING = False
                            else:
                                print("Le nombre de caisses doit être le même que de points")
                        else:
                            print("Il doit y avoir un joueur minimum et maximum")

                    if x <= 9 and y <= 9:
                        self.board[y][x] = self.cursor
                    self.draw_board()

                if event.type == pygame.QUIT:
                    self.RUNNING = False

    def draw_board(self):
        self.player = 0
        self.crates = 0
        self.points = 0
        y = x = 0
        # Draw ground
        for r in range(self.grid_size):
            self.screen.blit(self.sprites[0], (y, x))
            x = 0
            for c in range(self.grid_size):
                self.screen.blit(self.sprites[0], (y, x))
                x += self.tile_size
            y += self.tile_size
        # Draw Features
        y = x =0
        for r in range(len(self.board)):
            x = 0
            for c in range(len(self.board[r])):
                if self.board[r][c] == 2:
                    self.crates += 1
                elif self.board[r][c] == 3:
                    self.points += 1
                elif self.board[r][c] == 4:
                    self.player += 1
                self.screen.blit(self.sprites[self.board[r][c]], (x, y))

                x += self.tile_size
            y += self.tile_size

        self.draw_menu()

    def draw_menu(self):
        self.screen.blit(self.sprites[0], (1080, 20))
        self.screen.blit(self.sprites[1], (1080, 120))
        self.screen.blit(self.sprites[2], (1080, 220))
        self.screen.blit(self.sprites[3], (1080, 320))
        self.screen.blit(self.sprites[4], (1080, 420))
        self.screen.blit(self.sprites[5], (1080, 620))
