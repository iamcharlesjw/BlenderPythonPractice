# inspired by: https://www.youtube.com/shorts/wc6dpx9I0Is?feature=share

# give Python access to Blender's functionality
import bpy

# delete previously create object from last script run
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# add a cube into the scene
bpy.ops.mesh.primitive_cube_add()

# get a reference to the currently active objectcu
obj = bpy.context.active_object

#scale the cube mesh
obj.scale.x *= 0.5
obj.scale.y *= 0.5
obj.scale.z *= 0.5

#apply scale
bpy.ops.object.transform_apply()

# number of rows
row = 1
currentY = 0
currentX = 0

# stack and rotate the mesh
while row <= 10:
    for i in range(10):
        # duplicate the mesh
        bpy.ops.object.duplicate(linked=True)
        
        # get a reference to the currently active object
        dupObj = bpy.context.active_object
        
        # update the location of the object on the x and y axis
        dupObj.location.x += dupObj.dimensions.x*2
        dupObj.location.y = currentY

    # update x and y axis values for the next iteration
    currentY += obj.dimensions.y*2
    bpy.context.active_object.location.x = 0
    row += 1