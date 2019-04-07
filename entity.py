class Entity:
    def __init__(self, x, y, char, fg_color, bg_color, info, height, temp, magic):
        self.x = x
        self.y = y
        self.char = char
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.info = info
        self.height = height
        self.temp = temp
        self.magic = magic

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
