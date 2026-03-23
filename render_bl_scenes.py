import bpy
import sys
import os
import numpy as np

def blenderLoadScene(scenePath):
    bpy.ops.wm.open_mainfile(filepath=os.path.abspath(scenePath))

def initBlenderGlassMat():
    mat = bpy.data.materials.new("glass")
    mat.use_nodes = True
    mat.node_tree.nodes.clear()
    outputMat = mat.node_tree.nodes.new("ShaderNodeOutputMaterial")
    glass = mat.node_tree.nodes.new("ShaderNodeBsdfGlass")
    glass.inputs['Color'].default_value = (0, 0, 1, 1)
    mat.node_tree.links.new(glass.outputs[0], outputMat.inputs[0])

    return mat

def updateMatRoughness(mat, shader_node_name, roughness):
    shader = mat.node_tree.nodes[shader_node_name]
    shader.inputs['Roughness'].default_value = roughness

def prepareRenderer():
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.cycles.max_bounces = 1
    bpy.context.scene.cycles.samples = 64
    
def set_mat(obj_name, mat):
    bpy.data.objects[obj_name].active_material = mat

def main(scenePath, roughnessSpace, output):
    blenderLoadScene(scenePath)
    prepareRenderer()

    my_mat = initBlenderGlassMat()
    set_mat('controller', my_mat)
    
    for r in np.linspace(0, 1, roughnessSpace):
        updateMatRoughness(my_mat, 'Glass BSDF', r)
        outputFile = os.path.join(output, f"glass_r{r}.png")
        bpy.context.scene.render.filepath = os.path.abspath(outputFile)
        
        assert bpy.ops.render.render(write_still=True) == {"FINISHED"}

if __name__ == "__main__":
    args = sys.argv[sys.argv.index('--') + 1:]
    main(args[0], int(args[1]), args[2])