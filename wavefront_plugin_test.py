import mitsuba as mi
mi.set_variant('cuda_ad_rgb')

from mitsuba import ScalarTransform4f as T

import matplotlib.pyplot as plt

scene = mi.load_dict({
    'type': 'scene',
    'integrator': {'type': 'path'},
    'light': {'type': 'constant'},
    'fromBlend': {
        'type': 'ply',
        'filename': 'test_scene.ply',
        'flip_normals': False
    }
})

sensor = mi.load_dict({
    'type': 'perspective',
    'fov': 39.3077,
    'to_world': T().look_at(
        origin=T().rotate([0, 0, 1], 20.).rotate([0, 1, 0], 60.) @ mi.ScalarPoint3f([0, 0, 12]),
        target=[0, 0, 0],
        up=[0, 0, 1]
    ),
    'sampler': {
        'type': 'independent',
        'sample_count': 16
    },
    'film': {
        'type': 'hdrfilm',
        'width': 256,
        'height': 256,
        'rfilter': {
            'type': 'tent',
        },
        'pixel_format': 'rgb',
    },
})

img = mi.render(scene, sensor=sensor)

plt.axis('off')
plt.imshow(img ** (1.0 / 2.2))
plt.show()