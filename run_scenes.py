import mitsuba as mi
mi.set_variant('cuda_ad_rgb')

import sys
import glob

def main(path):
    files = glob.glob(f"{path}/*.xml")
    for f in files:
        f_type = f.split('/')[-1].split(".")[0]
        if f_type != "mix_same":
            continue
        
        scene = mi.load_file(f)
        img = mi.render(scene, spp=64)
        
        mi.util.write_bitmap(f"renders/{f_type}_mitsuba.png", img)

if __name__ == "__main__":
    main(sys.argv[1])