# Project journal and notes

## Next Step of the project

1. Complete tests suit for exporter and fix mae/mse (find error threshold + remove opencv)
2. Get plugins for blender shader node that was already done + try exporting one of the test scene. If needed create new plugin for unsupported shader node

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

## Quantify difference between two renders

Define $r_1$ and $r_2$ as the two RGB renders we want to compare, a pixel $i$ of render $r_k$ as $p_{i, k}$, $N$ as the total number of pixel in a render and $Y_i$ the random variable representing the difference between pixels $p_{i, 1}$ and $p_{i, 2}$, $Y_i = p_{i, 1} - p_{i, 2}$ 

Different possible error function to describe the difference between renders $r_1$ and $r_2$:
- Absolute error: $AE(r_1, r_2) = \sum_{n = 1}^N \| Y_n \|_1$
- Mean absolute error: $MAE(r_1, r_2) = \frac{1}{N} \sum_{n = 1}^N \| Y_n \|_1$
- Squared error: $SE(r_1, r_2) = \sum_{n = 1}^N \| Y_n \|_2^2$
- Mean squared error: $MSE(r_1, r_2) = \frac{1}{N} \sum_{n = 1}^N \| Y_n \|_2^2$

I think we are more interested in the average of pixel error rather than sum of all errors. MAE and MSE being average could also be seen as mean $\mu_1$, $\mu_2$ of respectively random variable $X_{i, 1} = \| Y_n \|_1$, $X_{i, 2} = \| Y_n \|_2²$ which can be used to compute a standard deviation.

For visual representation we can also display the image in grayscale based of the values of $X_{i, k}$ to see what part of the renders differs and how much.

We settled for MSE.

### Error threshold

Using a small script I rendered 100 mitsuba image from the same scene with different seed and computed the difference between every pair of renders and got the mean error, which is 0.00030549866250067045. Hence I will use a threshold of 0.000306 to consider two image identical.

## Exporting scene AI043_005

- Blender mesh chair_001 has invalid normals, can't instantiate mitsuba shape plugin "blender". Recalculate normals inside blender did not fix the issue. For now remove mesh to see what else is not working.
- Error tuple index out of range in io/exporter/material.py, line 451: Reason was no code to handle degenerate materials not linked.
- Mesh plants_001 also have invalid normals in mitsuba. For now same solution has above.
- Mesh plants_002, plants_003, plants_004, plants_005, invalid normals

Now successfully exported **BUT**

- Error when loading exported file: failed to instantiate sensor plugin of type "perspective": [PerspectiveCamera] Scale factors in the camera-to-world transformation are not allowed!
- A lot of materials use a node of type 'VALTORGB' which is not yet supported. 
- Brighcontrast node used which is not supported (an implementation exist on git branch blender_shader_node_textures)
- Mix node used which is not supported
- Bsdf_translucent node used which is not supported
- Curve_rgb node used which is not supported
- Bsdf_refraction node used which is not supported

## Remarks/notes

- One bounce in blender scene does not translate well to mitsuba (Single bounce in mitsuba generate black pictures)
- Headless blender still require to download blender's binary (bpy python package is not sufficient)

## TODO
- [x] Get back and working test suit
- [x] Redo tests with single max bounce (see remarks section)
- [x] Test with different roughness parameter
- [ ] Create list of difference between blender and mitsuba renders
- [x] Test l2_error function and assert its correctness
- [x] Upgrade glass test to function with other shader node
- [x] Compute error for identical images
- [x] look how to get principled plugin for blender principled bsdf
- [x] Support for Bright contrast nodes
- [ ] Support for bsdf principled nodes
    - Mitsuba plugin form Sebastien added, but is currently not working
- [ ] Support for color ramp (VALTORGB) nodes 
    - No mitsuba plugin exists for it, require complete implementation.
- [ ] Support for Mix color nodes
    - No mitsuba plugin exists for it, require complete implementation.
- [ ] Support for Bsdf translucent nodes
    - No mitsuba plugin exists for it, require complete implementation. Mitsuba 1 implemented it, can check there for inspiration.
- [x] Support for curve rgb nodes  
- [ ] Support for Bsdf refraction nodes
    - No mitsuba plugin exists for it, require complete implementation. Seems to be a simplified version of rough dielectric
- [ ] Bright contrast nodes and curve rgb nodes render differently in mi than bl, need to investigate  
