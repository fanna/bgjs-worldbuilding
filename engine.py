import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all
from palette import palette
from world_generator import get_world

def main():
    screen_width = 80
    screen_height = 80

    player = Entity(int(screen_width / 2), int(screen_height / 2), 'x', libtcod.red, libtcod.black, ' ')

    entities = get_world() + [player]

    libtcod.console_set_custom_font('data/fonts/terminal12x12_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_CP437)

    root_console = libtcod.console_init_root(screen_width, screen_height, 'BGJS: Worldbuilding', False, libtcod.RENDERER_SDL2, order="F")

    console = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(console, entities, screen_width, screen_height)

        libtcod.console_flush()

        clear_all(console, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx, dy)
            #FIXME: This is super inefficient but it is a product of game jam
            for entity in entities:
                if (entity.get_info() != ' '):
                    if (player.x == entity.x and player.y == entity.y):
                        console.print_frame(64, 0, 16, 64, '', True, 13)
                        console.print(65, 1, entity.char, entity.fg_color, entity.bg_color, libtcod.LEFT)
                        console.print(65, 3, entity.get_info(), libtcod.white, libtcod.black, libtcod.LEFT)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
