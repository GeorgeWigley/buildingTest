import bpy
import json

jsonOutputDict = {
    "buildings": []
}


# function that returns a dictionary of instance transforms, runs on currently slected footprint without geometry nodes
# applied
def GenerateInstancesDictForFootprint():
    # Add geo nodes
    gnmod = obj.modifiers.new("Buildify", "NODES")

    # Add correct node group
    gnmod.node_group = bpy.data.node_groups['building']

    # Create a dictionary to hold the instance data
    instance_dict = {}

    depsgraph = bpy.context.evaluated_depsgraph_get()
    for inst in depsgraph.object_instances:
        if inst.is_instance:
            # have correctly found instance, check if it's in the dict
            if inst.object.name not in instance_dict:
                instance_dict[inst.object.name] = []

            positionX = inst.matrix_world.to_translation()[0]
            positionY = inst.matrix_world.to_translation()[0]
            positionZ = inst.matrix_world.to_translation()[0]

            rotationX = inst.matrix_world.to_euler()[0]
            rotationY = inst.matrix_world.to_euler()[0]
            rotationZ = inst.matrix_world.to_euler()[0]

            scaleX = inst.matrix_world.to_scale()[0]
            scaleY = inst.matrix_world.to_scale()[0]
            scaleZ = inst.matrix_world.to_scale()[0]

            instance_dict[inst.object.name].append({
                "position": [positionX, positionY, positionZ],
                "eulerAngles": [rotationX, rotationY, rotationZ],
                "scale": [scaleX, scaleY, scaleZ]
            })
    return instance_dict

# Read JSON file
with open('C:/Users/George.000/Desktop/My project/blenderTest/inputs/testInput.json', 'r') as file:
    data = json.load(file)

# Parse footprints
for fp in data['footprints']:
    verts = fp['verts']
    facesUnparsed = fp['faces']
    faces = []
    height = fp['height']
    levels = fp['levels']
    # faces must be parsed into tuples
    for i in range(0, len(facesUnparsed), 3):
        faces.append(tuple(facesUnparsed[i:i + 3]))

    print(verts)
    print(faces)
    input()

    # Create Mesh Datablock
    mesh = bpy.data.meshes.new("test")
    mesh.from_pydata(verts, [], faces)

    # Create Object and link to scene
    obj = bpy.data.objects.new("testobj", mesh)
    bpy.context.scene.collection.objects.link(obj)

    # select object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # get instances into dict
    instances = GenerateInstancesDictForFootprint()
    # get into correct format
    formattedInstances = {
        "prefabs": []
    }

    for key, value in instances.items():
        formattedInstances["prefabs"].append({
            "name": key,
            "transforms": value
        })

    # add dict to jsonOutputDict
    jsonOutputDict["buildings"].append(formattedInstances)

# save to file
with open("C:/Users/George.000/Desktop/My project/blenderTest/outputs/testOutput.json", "w") as f:
    json.dump(jsonOutputDict, f, indent=4)
