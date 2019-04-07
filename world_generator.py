import tcod as libtcod
from noise import create_noise
from entity import Entity
from palette import palette

samples = create_noise()


def get_world():
    entities = []
    for i, sample in enumerate(samples, start=0):
        for j, num in enumerate(sample, start=0):
            terrain_type = get_type(num)
            entity = Entity(i, j, terrain_type.get('char'), terrain_type.get('color').get('fg'), terrain_type.get('color').get('bg'))
            entities.append(entity)
    return entities


def get_type(num):
    if (num < -0.7):
        color = palette[7]
        char = '≈'
    elif (num < -0.5 and num > -0.7):
        color = palette[1]
        char = '≈'
    elif (num > -0.5 and num < -0.3):
        color = palette[6]
        char = '.'
    elif (num > -0.2 and num < -0.1):
        color = palette[2]
        char = '.'
    elif (num > -0.1 and num < 0.1):
        color = palette[5]
        char = ','
    elif(num > 0.1 and num < 0.4):
        color = palette[0]
        char = '♠'
    elif(num > 0.4 and num < 0.6):
        color = palette[3]
        char = '▲'
    elif(num > 0.6):
        color = palette[4]
        char = '▲'
    else:
        color = palette[0]
        char = '♠'
    return {'color': color, 'char': char}

