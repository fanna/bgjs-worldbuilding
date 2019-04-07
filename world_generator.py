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
            entity = Entity(i, j, terrain_type.get('char'), terrain_type.get('color').get('fg'), terrain_type.get('color').get('bg'), info, terrain_type.get('height'), terrain_type.get('temp'), terrain_type.get('magic'))
            entities.append(entity)
    return entities


def get_type(num):
    if (num < -0.7):
        color = palette[7]
        char = '≈'
        info = 'Deep Water'
        height = np.random.uniform(-10.0, -3.0)
        temp = 3 if height > -5.0 else 0
        magic = '•' * np.random.randint(1, 4)
    elif (num < -0.5 and num > -0.7):
        color = palette[1]
        char = '≈'
        info = 'Shallow Water'
        height = np.random.uniform(-2.0, -0.2)
        temp = 20
        magic = '•' * np.random.randint(1, 4)
    elif (num > -0.5 and num < -0.3):
        color = palette[6]
        char = '.'
        info = 'Sand'
        height = np.random.uniform(0.0, 0.3)
        temp = 30
        magic = '•' * np.random.randint(1, 4)
    elif (num > -0.2 and num < -0.1):
        color = palette[2]
        char = '.'
        info = 'Dirt'
        height = np.random.uniform(0.0, 1.0)
        temp = 28
        magic = '•' * np.random.randint(1, 4)
    elif (num > -0.1 and num < 0.1):
        color = palette[5]
        char = ','
        info = 'Grass'
        height = np.random.uniform(0.0, 1.0)
        temp = 26
        magic = '•' * np.random.randint(1, 4)
    elif(num > 0.1 and num < 0.4):
        color = palette[0]
        char = '♠'
        info = 'Spring Tree'
        height = np.random.randint(2, 10)
        temp = 20 if height > 5 else 25
        magic = '•' * np.random.randint(1, 4)
    elif(num > 0.4 and num < 0.6):
        color = palette[3]
        char = '▲'
        info = 'Mountain'
        height = np.random.randint(250, 800)
        temp = 18 if height < 500 else 12
        magic = '•' * np.random.randint(1, 4)
    elif(num > 0.6):
        color = palette[4]
        char = '▲'
        info = 'High Mountain'
        height = np.random.randint(800, 2800)
        temp = 3 if height < 1500 else -2
        magic = '•' * np.random.randint(1, 4)
    else:
        color = palette[0]
        char = '♠'
        info = 'Spring Tree'
        height = np.random.randint(2, 10)
        temp = 20 if height > 5 else 25
        magic = '•' * np.random.randint(1, 4)
    return {'color': color, 'char': char, 'info': info, 'height': np.round(height, 2), 'temp': temp, 'magic': magic}

