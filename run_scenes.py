import mitsuba as mi
mi.set_variant('cuda_ad_rgb')

import sys

def main(shader_type):
    scene = mi.load_file(f"mitsuba_scenes/{shader_type}.xml")
    img = mi.render(scene, spp=64)

    mi.util.write_bitmap(f"{shader_type}_mitsuba.png", img)

if __name__ == "__main__":
    main(sys.argv[1])