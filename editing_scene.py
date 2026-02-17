import drjit as dr
import mitsuba as mi
import matplotlib.pyplot as plt

def main():
    mi.set_variant('llvm_ad_rgb')

    scene = mi.load_file('scenes/simple.xml')

    base_img = mi.render(scene)

    param = mi.traverse(scene)
    print(param)

    param["light1.intensity.value"] *= [1.5, 0.2, 0.2]
    param["light2.intensity.value"] *= [0.2, 1.5, 0.2]

    v = dr.unravel(mi.Point3f, param['teapot.vertex_positions'])
    v.z += 0.5
    param["teapot.vertex_positions"] = dr.ravel(v)

    param.update()

    new_img = mi.render(scene)

    fig = plt.figure(figsize=(10, 10))
    fig.add_subplot(1,2,1).imshow(base_img); plt.axis('off'); plt.title('original')
    fig.add_subplot(1,2,2).imshow(new_img); plt.axis('off'); plt.title('modified');
    plt.show()

if __name__ == '__main__':
    main()