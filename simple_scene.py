import mitsuba as mi
mi.set_variant('cuda_ad_rgb')
print(mi.__version__)

import matplotlib.pyplot as plt

scene = mi.load_file('simple_xml.xml')
# scene = mi.load_dict({
#     'type': 'scene',
#     'integrator': {'type': 'path', 'max_depth': 5},
#     'area_light': {
#         'type': 'sphere',
#         'emitter': {
#             'type': 'area',
#             'radiance': {
#                 'type': 'rgb',
#                 'value': [100, 100, 100],
#             },
#         },
#         'to_world': mi.ScalarTransform4f().translate([-1, 2, 2]).scale(0.2)
#     },
#     'object': {
#         'type': 'cube',
#         'shading': {
#             'type': 'diffuse',
#             'reflectance': {
#                 'type': 'rgb',
#                 'value': [1, 0.0, 0.0],
#             },
#         },
#     },
#     'cam': {
#         'type': 'perspective',
#         'fov': 45,
#         'to_world': mi.ScalarTransform4f().look_at(
#             origin=[0, 10, 2],
#             target=[0, 0, 0],
#             up=[0, 0, 1]
#         ),
#         'sampler': {
#         'type': 'independent',
#         'sample_count': 16
#         },
#         'film': {
#             'type': 'hdrfilm',
#             'width': 512,
#             'height': 512,
#             'rfilter': {
#                 'type': 'tent',
#             },
#             'pixel_format': 'rgb',
#         },
#     }
# })

img = mi.render(scene)

plt.axis('off')
plt.imshow(img ** (1.0 / 2.2))
plt.show()