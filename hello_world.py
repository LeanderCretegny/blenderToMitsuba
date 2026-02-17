import mitsuba as mi
import matplotlib as plt

def main():
    mi.set_variant('scalar_rgb')

    img = mi.render(mi.load_dict(mi.cornell_box()))

    plt.axis("off")
    plt.im

if __name__ == "__main__":
    main()