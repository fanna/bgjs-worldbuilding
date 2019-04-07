import numpy as np
import tcod
import tcod.noise

def create_noise():
    noise = tcod.noise.Noise(
            dimensions=2,
            algorithm=tcod.NOISE_PERLIN,
            implementation=tcod.noise.SIMPLE,
            hurst=0.5,
            lacunarity=2.0,
            octaves=4,
            seed=None,
            )

    ogrid = [np.arange(64, dtype=np.float32),
            np.arange(64, dtype=np.float32)]
    print(ogrid)

    ogrid[0] *= 0.25
    ogrid[1] *= 0.25

    samples = noise.sample_ogrid(ogrid)
    print(samples)
    return samples
