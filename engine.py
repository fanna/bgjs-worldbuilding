import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all
from noise import create_noise
from palette import palette
from world_generator import get_world

def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width / 2), int(screen_height / 2), 'x', libtcod.red, libtcod.black)

    world = get_world()
    entities = world + [player]

    libtcod.console_set_custom_font('data/fonts/terminal8x8_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_CP437)

    libtcod.console_init_root(screen_width, screen_height, 'BGJS: Worldbuilding', False)

    console = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    create_noise()

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

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
