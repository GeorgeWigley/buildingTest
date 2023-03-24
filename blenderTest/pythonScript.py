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

verts = [[0,0,0], [0,10,0], [10,0,0], [10,10,0]]
faces = [(0,2,1),(2,3,1)]

# Create Mesh Datablock
mesh = bpy.data.meshes.new("test")
mesh.from_pydata(verts, [], faces)

# Create Object and link to scene
obj = bpy.data.objects.new("testobj", mesh)
bpy.context.scene.collection.objects.link(obj)

bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Add geo nodes
gnmod = obj.modifiers.new("Buildify", "NODES")

# Add correct node group
gnmod.node_group = bpy.data.node_groups['building']

# convert to mesh
bpy.ops.object.duplicates_make_real(use_base_parent=True, use_hierarchy=True)

# Export Mesh
bpy.ops.export_scene.gltf(filepath="C:/Users/zk20435/Documents/buildingTest/blenderTest/outputs/test.gltf", export_format="GLTF_EMBEDDED", check_existing=False, use_selection=True)
