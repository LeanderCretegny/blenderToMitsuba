import mitsuba as mi
import matplotlib.pyplot as plt

def main():
    mi.set_variant('scalar_rgb')

    img = mi.render(mi.load_dict(mi.cornell_box()), spp=256)

    plt.axis("off")
    plt.imshow(img ** (1.0 / 2.2))
    plt.show()

if __name__ == "__main__":
    main()