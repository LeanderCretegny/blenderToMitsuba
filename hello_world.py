import mitsuba as mi

def main():
    mi.set_variant('scalar_rgb')

    img = mi.render(mi.load_dict(mi.cornell_box()))

    mi.Bitmap(img).write('cbox.exr')

if __name__ == "__main__":
    main()