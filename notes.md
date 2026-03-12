# Project journal and notes
## Current state of plugin

- On branch [mitsuba_version_update](https://github.com/mitsuba-renderer/mitsuba-blender/pull/137)
- Works with mitsuba 3.7 
- Internal rendering: not working at all (in blender lts 3 it raises unhandled error by invocating deprecated functions, in blender lts 4 the mitsubaRenderEngine class is simply incorect, was made for blender 3)
- Import: meshes seems to be correctly imported but materials are lost when trying to use mitsuba as render engine. Other engine keep some material but not all => requires more testing
- Export: meshes seems to be correctly exported to mitsuba, however light and material might not. Further testing is required.

### Export tests 
Blender scenes rendered with cycles using 64 samples and 5 bounces 
| shader node | export to mitsuba works | visually similar | Blender (Cycle) | Mitsuba |
|-|-|-|-|-|
| Diffuse + point light | yes | yes | <img width="200" src="renders/diffuse_pl_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_pl_mitsuba.png" alt="mitsuba"> |
| diffuse + sun | yes | no | <img width="200" src="renders/diffuse_sun_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_sun_mitsuba.png" alt="mitsuba"> |
| diffuse + spot | yes | yes | <img width="200" src="renders/diffuse_spot_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_spot_mitsuba.png" alt="mitsuba"> |
| diffuse + area | yes | yes but light visible in mi | <img width="200" src="renders/diffuse_area_blender.png" alt="blender"> | <img width="200" src="renders/diffuse_area_mitsuba.png" alt="mitsuba"> |
| Emission + metallic bsdf | yes | slight differences | <img width="200" src="renders/emission_blender.png" alt="blender"> | <img width="200" src="renders/emission_mitsuba.png" alt="mitsuba"> |
| Glass + sun light + diffuse plane | yes | no | <img width="200" src="renders/glass_blender.png" alt="blender"> | <img width="200" src="renders/glass_mitsuba.png" alt="mitsuba"> |
| Glossy | yes | slight differences | <img width="200" src="renders/glossy_blender.png" alt="blender"> | <img width="200" src="renders/glossy_mitsuba.png" alt="mitsuba"> |
| Metallic | no | - | <img width="200" src="renders/metallic_blender.png" alt="blender"> | <img width="200" src="renders/metallic_mitsuba.png" alt="mitsuba"> |
| Mix | no | - | <img width="200" src="renders/mix_blender.png" alt="blender"> | <img width="200" src="renders/mix_mitsuba.png" alt="mitsuba"> |
| Principled | no | - | <img width="200" src="renders/principled_blender.png" alt="blender"> | <img width="200" src="renders/principled_mitsuba.png" alt="mitsuba"> |
| Ray portal | no | - | <img width="200" src="renders/ray_portal_blender.png" alt="blender"> | <img width="200" src="renders/ray_portal_mitsuba.png" alt="mitsuba"> |
| Refraction | no | - | <img width="200" src="renders/refraction_sun_blender.png" alt="blender"> | <img width="200" src="renders/refraction_sun_mitsuba.png" alt="mitsuba"> |
| Sub surface scattering | no | - | <img width="200" src="renders/subsurf_blender.png" alt="blender"> | <img width="200" src="renders/subsurf_mitsuba.png" alt="mitsuba"> |
| Toon | no | - | <img width="200" src="renders/toon_blender.png" alt="blender"> | <img width="200" src="renders/toon_mitsuba.png" alt="mitsuba"> |
| translucent | no | - | <img width="200" src="renders/translucent_blender.png" alt="blender"> | <img width="200" src="renders/translucent_mitsuba.png" alt="mitsuba"> |
| Transparent | yes | no | <img width="200" src="renders/transparent_blender.png" alt="blender"> | <img width="200" src="renders/transparent_mitsuba.png" alt="mitsuba"> |
| Volume scatter | no | - | <img width="200" src="renders/vol_scatter_blender.png" alt="blender"> | <img width="200" src="renders/vol_scatter_mitsuba.png" alt="mitsuba"> |

- Bug encountered when exporting volume scatter 
- Bug encountered when mitsuba tried rendering principled 