import mitsuba as mi
mi.set_variant('cuda_ad_rgb')

import matplotlib.pyplot as plt

scene = mi.load_file('test_scene.xml')
print(mi.traverse(scene))

img = mi.render(scene, spp=256)

plt.axis('off')
plt.imshow(img)
plt.show()