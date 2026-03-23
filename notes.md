# Project journal and notes
## Current state of plugin

- On branch [mitsuba_version_update](https://github.com/mitsuba-renderer/mitsuba-blender/pull/137)
- Works with mitsuba 3.7 
- Internal rendering: not working at all (in blender lts 3 it raises unhandled error by invocating deprecated functions, in blender lts 4 the mitsubaRenderEngine class is simply incorect, was made for blender 3)
- Import: meshes seems to be correctly imported but materials are lost when trying to use mitsuba as render engine. Other engine keep some material but not all => requires more testing
- Export: meshes seems to be correctly exported to mitsuba, however light and material might not. Further testing is required.

### Export tests 
Blender scenes rendered with cycles using 64 samples and 5 bounces 

| shader node | expected to work based on [wiki](https://github.com/mitsuba-renderer/mitsuba-blender/wiki/Exporting-a-Blender-scene) | export to mitsuba works | visually similar | Blender (Cycle) | Mitsuba |
|-|-|-|-|-|-|
| Diffuse + point light | yes | yes | yes | <img width="200" src="renders/diffuse_pl_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_pl_mitsuba.png" alt="mitsuba"> |
| diffuse + sun | yes | yes | no | <img width="200" src="renders/diffuse_sun_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_sun_mitsuba.png" alt="mitsuba"> |
| diffuse + spot | yes |yes | yes | <img width="200" src="renders/diffuse_spot_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_spot_mitsuba.png" alt="mitsuba"> |
| diffuse + area | yes | yes | yes but light visible in mi | <img width="200" src="renders/diffuse_area_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_area_mitsuba.png" alt="mitsuba"> |
| diffuse + area rectangle | yes | yes | yes but light visible in mi | <img width="200" src="renders/area_rect_blender.png" alt="blender"> | <img width="200" src="renders/area_rect_mitsuba.png" alt="mitsuba"> |
| diffuse + area disk | yes | yes | yes but light visible in mi | <img width="200" src="renders/area_disk_blender.png" alt="blender"> | <img width="200" src="renders/area_disk_mitsuba.png" alt="mitsuba"> |
| diffuse + area ellipse | no | no | - | <img width="200" src="renders/area_ell_blender.png" alt="blender"> | <img width="200" src="renders/area_ell_mitsuba.png" alt="mitsuba"> |
| Emission + metallic bsdf | yes | yes | slight differences | <img width="200" src="renders/emission_blender.png" alt="blender"> | <img width="200" src="renders/emission_mitsuba.png" alt="mitsuba"> |
| Glass + sun light + diffuse plane | yes | yes | no | <img width="200" src="renders/glass_blender.png" alt="blender"> | <img width="200" src="renders/glass_mitsuba.png" alt="mitsuba"> |
| Glossy | yes | yes | slight differences | <img width="200" src="renders/glossy_blender.png" alt="blender"> | <img width="200" src="renders/glossy_mitsuba.png" alt="mitsuba"> |
| Metallic | no |no | - | <img width="200" src="renders/metallic_blender.png" alt="blender"> | <img width="200" src="renders/metallic_mitsuba.png" alt="mitsuba"> |
| Mix (diffuse + diffuse) | yes | no | - | <img width="200" src="renders/mix_same_blender.png" alt="blender"> | <img width="200" src="renders/mix_same_mitsuba.png" alt="mitsuba"> |
| Mix (diffuse + glass) | yes | no | - | <img width="200" src="renders/mix_blender.png" alt="blender"> | <img width="200" src="renders/mix_mitsuba.png" alt="mitsuba"> |
| Principled | yes | no | - | <img width="200" src="renders/principled_blender.png" alt="blender"> | <img width="200" src="renders/principled_mitsuba.png" alt="mitsuba"> |
| Ray portal | no | no | - | <img width="200" src="renders/ray_portal_blender.png" alt="blender"> | <img width="200" src="renders/ray_portal_mitsuba.png" alt="mitsuba"> |
| Refraction | no | no | - | <img width="200" src="renders/refraction_sun_blender.png" alt="blender"> | <img width="200" src="renders/refraction_sun_mitsuba.png" alt="mitsuba"> |
| Sub surface scattering | no | no | - | <img width="200" src="renders/subsurf_blender.png" alt="blender"> | <img width="200" src="renders/subsurf_mitsuba.png" alt="mitsuba"> |
| Toon | no | no | - | <img width="200" src="renders/toon_blender.png" alt="blender"> | <img width="200" src="renders/toon_mitsuba.png" alt="mitsuba"> |
| translucent | no | no | - | <img width="200" src="renders/translucent_blender.png" alt="blender"> | <img width="200" src="renders/translucent_mitsuba.png" alt="mitsuba"> |
| Transparent | no | yes | no | <img width="200" src="renders/transparent_blender.png" alt="blender"> | <img width="200" src="renders/transparent_mitsuba.png" alt="mitsuba"> |
| Volume scatter | no | no | - | <img width="200" src="renders/vol_scatter_blender.png" alt="blender"> | <img width="200" src="renders/vol_scatter_mitsuba.png" alt="mitsuba"> |
| Metaball | yes | not really | artefact creation | <img width="200" src="renders/meta_blender.png" alt="blender"> | <img width="200" src="renders/meta_mitsuba.png" alt="mitsuba"> |
| Text | yes | no | duplicate text | <img width="200" src="renders/text_blender.png" alt="blender"> | <img width="200" src="renders/text_mitsuba.png" alt="mitsuba"> |
| Nurbs surface | yes | no | duplicate surface | <img width="200" src="renders/nurbs_blender.png" alt="blender"> | <img width="200" src="renders/nurbs_mitsuba.png" alt="mitsuba"> |
| Image texture | yes | yes | yes | <img width="200" src="renders/tex_blender.png" alt="blender"> | <img width="200" src="renders/tex_mitsuba.png" alt="mitsuba"> |
| Vertex color | yes | no | - | <img width="200" src="renders/vertex_blender.png" alt="blender"> | <img width="200" src="renders/vertex_mitsuba.png" alt="mitsuba"> |
| Environment map | yes | yes | yes | <img width="200" src="renders/environment_blender.png" alt="blender"> | <img width="200" src="renders/environment_mitsuba.png" alt="mitsuba"> |


- Bug encountered when exporting volume scatter 
- Bug encountered when mitsuba tried rendering principled scene 

### How to test correctness of plugin
- Do we care about getting same renders as done inside of blender? YES
- Naive idea: Generate render in mitsuba using export of  predetermined blender tests scene, then compare result with reference (can be a previously rendered image of said scene). But how to compare the images? Question asked in previous semester project can go look into that. => **Not that interesting, would like to detect change on the blender side, want to compare blender and mitsuba renders directly with error factor**

### Current state of tests

- All tests run and pass if mitsuba-blender addon is not installed in blender (if it is installed, run_test.py crashes)
- Total coverage is 49%
- Most tests done on the importer, almost no test on the export
- Uses a z-test to compare between two mitsuba render (a reference and a new image generated from importing and exporting ref in and from blender)

<img src="cov_detail.png" alt="coverage detail">

## TODO

- Get back and working test suit
- Redo tests with single max bounce
- Test with different roughness parameter
- Create list of difference between blender and mitsuba renders
- Try generating blender renders from file (if possible not from .obj) by script inside tests