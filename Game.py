import pygame
from Player import Player

class Game:
    def __init__(self, board):
        self.RUNNING = True
        self.board = board
        self.screen = 0
        self.HEIGHT = self.WIDTH = 800
        self.ROWS = self.COLS = 10
        self.ROW_WIDTH = self.WIDTH // self.COLS
        self.COL_WIDTH = self.HEIGHT // self.ROWS
        self.sprites = []
        self.player_sprite = []
        self.player_pos = (0, 0)
        self.music = 0
        self.player = 0
        self.collide = 0
        self.grunt = 0
        self.move_crate = 0
        self.walk = 0
        self.crates = 0
        self.ranged_crate = 0
        self.win = 0

    def load(self):
        print("Chargement des images")
        crate = pygame.image.load('./PNG/crate.png')
        crate = pygame.transform.scale(crate, (self.ROW_WIDTH, self.COL_WIDTH))
        wall = pygame.image.load('./PNG/wall.png')
        wall = pygame.transform.scale(wall, (self.ROW_WIDTH, self.COL_WIDTH))
        ground = pygame.image.load('./PNG/ground.png')
        ground = pygame.transform.scale(ground, (self.ROW_WIDTH, self.COL_WIDTH))

        player_front = pygame.image.load('./PNG/player_front.png')
        player_front = pygame.transform.scale(player_front, (self.ROW_WIDTH, self.COL_WIDTH))
        player_back = pygame.image.load('./PNG/player_back.png')
        player_back = pygame.transform.scale(player_back, (self.ROW_WIDTH, self.COL_WIDTH))
        player_left = pygame.image.load('./PNG/player_left.png')
        player_left = pygame.transform.scale(player_left, (self.ROW_WIDTH, self.COL_WIDTH))
        player_right = pygame.image.load('./PNG/player_right.png')
        player_right = pygame.transform.scale(player_right, (self.ROW_WIDTH, self.COL_WIDTH))

        point = pygame.image.load('./PNG/point.png')
        point = pygame.transform.scale(point, (self.ROW_WIDTH, self.COL_WIDTH))
        self.player_sprite = [
            player_front,
            player_back,
            player_left,
            player_right
        ]
        self.sprites = [
            ground,
            wall,
            crate,
            point,
            self.player_sprite[0],
        ]
        print("Chargement des sons")
        self.music = pygame.mixer.Sound('music.wav')
        self.collide = pygame.mixer.Sound('collide.wav')
        self.grunt = pygame.mixer.Sound('grunt.wav')
        self.move_crate = pygame.mixer.Sound('crate_move.wav')
        self.walk = pygame.mixer.Sound('walk.wav')
        self.win = pygame.mixer.Sound('win.wav')

    def init(self):
        pygame.init()
        pygame.mixer.init()
        self.load()
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        pygame.display.set_caption('My Sokoban')
        pygame.display.set_icon(self.sprites[2])
        pygame.mixer.Sound.play(self.music)
        self.draw_board()
        self.init_player()

        while self.RUNNING:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.sprites[4] = self.player_sprite[2]
                        self.check_move(self.player.move_left())
                    if event.key == pygame.K_RIGHT:
                        self.sprites[4] = self.player_sprite[3]
                        self.check_move(self.player.move_right())
                    if event.key == pygame.K_UP:
                        self.sprites[4] = self.player_sprite[1]
                        self.check_move(self.player.move_up())
                    if event.key == pygame.K_DOWN:
                        self.sprites[4] = self.player_sprite[0]
                        self.check_move(self.player.move_down())


    def check_move(self, new_pos):
        new_player_y = new_pos[0]
        new_player_x = new_pos[1]
        current_player_y = self.player_pos[0]
        current_player_x = self.player_pos[1]

        if self.board[new_player_y][new_player_x] != 1:
            if self.board[new_player_y][new_player_x] == 2:
                crate_pos = (new_player_y, new_player_x)
                # Move up
                if crate_pos[0] < current_player_y:
                    if self.board[new_player_y - 1][crate_pos[1]] != 1:
                        if self.board[new_player_y - 1][crate_pos[1]] == 3:
                            pygame.mixer.Sound.play(self.win)
                            self.ranged_crate += 1
                        else:
                            self.board[new_player_y - 1][crate_pos[1]] = 2
                            self.board[current_player_y][current_player_x] = 0
                            self.board[new_player_y][new_player_x] = 4
                            self.player.pos = (new_player_y, new_player_x)
                            pygame.mixer.Sound.play(self.move_crate)
                    else:
                        pygame.mixer.Sound.play(self.grunt)
                # Move down
                elif crate_pos[0] > current_player_y:
                    if self.board[new_player_y + 1][crate_pos[1]] != 1:
                        if self.board[new_player_y + 1][crate_pos[1]] == 3:
                            self.ranged_crate += 1
                        self.board[new_player_y + 1][crate_pos[1]] = 2
                        self.board[current_player_y][current_player_x] = 0
                        self.board[new_player_y][new_player_x] = 4
                        self.player.pos = (new_player_y, new_player_x)
                        pygame.mixer.Sound.play(self.move_crate)
                    else:
                        pygame.mixer.Sound.play(self.grunt)
                # Move left
                elif crate_pos[1] < current_player_x:
                    if self.board[crate_pos[0]][new_player_x - 1] != 1:
                        if self.board[crate_pos[0]][new_player_x - 1] == 3:
                            self.ranged_crate += 1
                        self.board[crate_pos[0]][new_player_x - 1] = 2

                        self.board[current_player_y][current_player_x] = 0
                        self.board[new_player_y][new_player_x] = 4
                        self.player.pos = (new_player_y, new_player_x)
                        pygame.mixer.Sound.play(self.move_crate)
                    else:
                        pygame.mixer.Sound.play(self.grunt)
                # Move Right
                elif crate_pos[1] > current_player_x:
                    if self.board[crate_pos[0]][new_player_x + 1] != 1:
                        if self.board[crate_pos[0]][new_player_x + 1] == 3:
                            self.ranged_crate += 1
                        self.board[crate_pos[0]][new_player_x + 1] = 2

                        self.board[current_player_y][current_player_x] = 0
                        self.board[new_player_y][new_player_x] = 4
                        self.player.pos = (new_player_y, new_player_x)
                        pygame.mixer.Sound.play(self.move_crate)
                    else:
                        pygame.mixer.Sound.play(self.grunt)
            else:
                self.board[current_player_y][current_player_x] = 0
                self.board[new_player_y][new_player_x] = 4
                self.player.pos = (new_player_y, new_player_x)
                pygame.mixer.Sound.play(self.walk)
        else:
            pygame.mixer.Sound.play(self.collide)
        self.draw_board()
        if self.crates == 0:
            self.RUNNING = False
            print("You win !")

    def init_player(self):
        self.player = Player(self.player_pos)

    def draw_board(self):
        self.crates = 0
        y = x = 0
        for r in range(self.ROWS):
            self.screen.blit(self.sprites[0], (x, y))
            x = 0
            for c in range(self.COLS):
                self.screen.blit(self.sprites[0], (x, y))
                x += self.ROW_WIDTH
            y += self.COL_WIDTH
        y = x = 0
        for r in range(len(self.board)):
            x = 0
            for c in range(len(self.board[r])):
                if self.board[r][c] != 0:
                    self.screen.blit(self.sprites[self.board[r][c]], (x, y))
                if self.board[r][c] == 3:
                    self.crates += 1
                if self.board[r][c] == 4:
                    self.player_pos = (r, c)

                x += self.ROW_WIDTH
            y += self.ROW_WIDTH