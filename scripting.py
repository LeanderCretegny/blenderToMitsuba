import mitsuba as mi
import drjit as dr
import matplotlib.pyplot as plt

mi.set_variant('llvm_ad_rgb')

def main():
    scene = mi.load_file('scenes/cbox.xml')

    cam_origin = mi.Point3f(0, 1, 3)
    cam_dir = dr.normalize(mi.Vector3f(0, -0.5, -1))
    cam_width = 2.
    cam_height = 2.

    img_res = (256, 256)

    # Grid of 2d coordinates
    x, y = dr.meshgrid(
        dr.linspace(mi.Float, -cam_width / 2, cam_width / 2, img_res[0]),
        dr.linspace(mi.Float, -cam_height / 2, cam_height / 2, img_res[1])
    )

    # Ray origin in local coord
    ray_l_origin = mi.Vector3f(x, y, 0)

    # Ray origin in world coord
    ray_w_origin = mi.Frame3f(cam_dir).to_world(ray_l_origin) + cam_origin

    ray = mi.Ray3f(o=ray_w_origin, d=cam_dir)
    si = scene.ray_intersect(ray)

    ambient_range = 0.75
    ambient_ray_count = 256

    rng = mi.PCG32(size=dr.prod(img_res))

    # Ambient occlusion result
    result = my_loop(mi.Float(0), scene, si, rng, ambient_ray_count, ambient_range)

    img = mi.TensorXf(result, shape=img_res)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()

@dr.syntax
def my_loop(res, scene, si, rng, ambient_ray_count, ambient_range):
    # loop counter
    i = mi.UInt32(0)

    while (si.is_valid() & (i < ambient_ray_count)):
        # draw random number
        sample1, sample2 = rng.next_float32(), rng.next_float32()

        # compute dir on local surface hemisphere
        wo_local = mi.warp.square_to_uniform_hemisphere([sample1, sample2])

        # get world coord of local sampled dir
        wo_world = si.sh_frame.to_world(wo_local)

        # spawn new ray at surface intersection
        ray2 = si.spawn_ray(wo_world)
        ray2.maxt = ambient_range

        res[~scene.ray_test(ray2)] += 1.

        i += 1
    
    return res / ambient_ray_count

if __name__ == '__main__':
    main()