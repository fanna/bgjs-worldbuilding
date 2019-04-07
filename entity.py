class Entity:
    def __init__(self, x, y, char, fg_color, bg_color):
        self.x = x
        self.y = y
        self.char = char
        self.fg_color = fg_color
        self.bg_color = bg_color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
