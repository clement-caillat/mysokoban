class Player:

    def __init__(self, pos):
        self.pos = pos
        self.move_right()

    def move_right(self):
        return (self.pos[0], self.pos[1] + 1)
    def move_left(self):
        return (self.pos[0], self.pos[1] - 1)
    def move_up(self):
        return (self.pos[0] - 1, self.pos[1])
    def move_down(self):
        return (self.pos[0] + 1, self.pos[1])