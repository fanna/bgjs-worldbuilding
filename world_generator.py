import tcod as libtcod
from noise import create_noise
from entity import Entity
from palette import palette
import numpy as np

def get_world():
    samples = create_noise()
    entities = []
    for i, sample in enumerate(samples, start=0):
        for j, num in enumerate(sample, start=0):
            terrain_type = get_type(num)
            info = terrain_type.get('info')
            entity = Entity(i, j, terrain_type.get('char'), terrain_type.get('color').get('fg'), terrain_type.get('color').get('bg'), info)
            entities.append(entity)
    return entities


def get_type(num):
    if (num < -0.7):
        color = palette[7]
        char = '≈'
        info = 'Deep Water'
    elif (num < -0.5 and num > -0.7):
        color = palette[1]
        char = '≈'
        info = 'Shallow Water'
    elif (num > -0.5 and num < -0.3):
        color = palette[6]
        char = '.'
        info = 'Sand'
    elif (num > -0.2 and num < -0.1):
        color = palette[2]
        char = '.'
        info = 'Dirt'
    elif (num > -0.1 and num < 0.1):
        color = palette[5]
        char = ','
        info = 'Grass'
    elif(num > 0.1 and num < 0.4):
        color = palette[0]
        char = '♠'
        info = 'Spring Tree'
    elif(num > 0.4 and num < 0.6):
        color = palette[3]
        char = '▲'
        info = 'Mountain'
    elif(num > 0.6):
        color = palette[4]
        char = '▲'
        info = 'High Mountain'
    else:
        color = palette[0]
        char = '♠'
        info = 'Cedar Tree'
    return {'color': color, 'char': char, 'info': info}

