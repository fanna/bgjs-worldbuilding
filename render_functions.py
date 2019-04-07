import tcod as libtcod

def render_all(console, entities, screen_width, screen_height):
    for entity in entities:
        draw_entity(console, entity)
    libtcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(console, entities):
    for entity in entities:
        clear_entity(console, entity)

def draw_entity(console, entity):
    libtcod.console_set_default_background(console, entity.bg_color)
    libtcod.console_set_default_foreground(console, entity.fg_color)
    libtcod.console_put_char(console, entity.x, entity.y, entity.char, libtcod.BKGND_SET)

def clear_entity(console, entity):
    libtcod.console_set_default_background(console, libtcod.black)
    libtcod.console_put_char(console, entity.x, entity.y, ' ', libtcod.BKGND_SET)
