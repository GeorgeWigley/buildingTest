import bpy

# Add test plane
#bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# Store ref to object
#activeObj = bpy.context.active_object

# Load demo file
bpy.ops.import_scene.fbx(filepath="C:/Users/George.000/Desktop/blenderTest/inputs/testFootprint.fbx")

# Store ref to object
activeObj = bpy.context.selected_objects[0]

# Add geo nodes
gnmod = activeObj.modifiers.new("Buildify", "NODES")

# Add correct node group
gnmod.node_group = bpy.data.node_groups['building']

# convert to mesh
bpy.ops.object.duplicates_make_real(use_base_parent=True, use_hierarchy=True)

# Export Mesh
bpy.ops.export_scene.gltf(filepath="C:/Users/George.000/Desktop/blenderTest/outputs/test.gltf", export_format="GLTF_EMBEDDED", check_existing=False, use_selection=True)
