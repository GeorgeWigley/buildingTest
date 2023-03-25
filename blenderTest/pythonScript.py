import bpy
import json

# Read JSON file
# with open('/inputs/testInput.json', 'r') as file:
#     data = json.load(file)
#
# # Parse footprints
# for fp in data['footprints']:
#     verts = fp['verts']
#     faces = fp['faces']
#     height = fp['height']
#     levels = fp['levels']

verts = [[0, 0, 0], [0, 10, 0], [10, 0, 0], [10, 10, 0]]
faces = [(0, 2, 1), (2, 3, 1)]

# Create Mesh Datablock
mesh = bpy.data.meshes.new("test")
mesh.from_pydata(verts, [], faces)

# Create Object and link to scene
obj = bpy.data.objects.new("testobj", mesh)
bpy.context.scene.collection.objects.link(obj)

# select object
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Add geo nodes
gnmod = obj.modifiers.new("Buildify", "NODES")

# Add correct node group
gnmod.node_group = bpy.data.node_groups['building']

# Create a dictionary to hold the instance data
instance_dict = {}

with open("C:/Users/George.000/Desktop/My project/blenderTest/outputs/testOutput.json", "w") as f:
    depsgraph = bpy.context.evaluated_depsgraph_get()
    for inst in depsgraph.object_instances:
        if (inst.is_instance):
            # have correctly found instance, check if it's in the dict
            if (inst.object.name not in instance_dict):
                instance_dict[inst.object.name] = []

            position = str(inst.matrix_world.to_translation()[0]) + ", " + \
                       str(inst.matrix_world.to_translation()[1]) + ", " + \
                       str(inst.matrix_world.to_translation()[2])

            rotation = str(inst.matrix_world.to_euler()[0]) + ", " + \
                       str(inst.matrix_world.to_euler()[1]) + ", " + \
                       str(inst.matrix_world.to_euler()[2])

            scale = str(inst.matrix_world.to_scale()[0]) + ", " + \
                    str(inst.matrix_world.to_scale()[1]) + ", " + \
                    str(inst.matrix_world.to_scale()[2])

            instance_dict[inst.object.name].append({
                "position": position,
                "rotation": rotation,
                "scale": scale
            })

    json.dump(instance_dict, f, indent=4)
