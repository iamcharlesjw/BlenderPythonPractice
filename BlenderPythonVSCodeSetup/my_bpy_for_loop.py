# code tutorial: https://www.youtube.com/watch?v=AcoYA4T2ErU

# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
# helps convert degrees to radians
import math

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
#add a cube mesh
bpy.ops.mesh.primitive_cube_add()

#get a reference to the currently active object
obj = bpy.context.active_object

#scale the cube mesh
obj.scale.x *= 0.5
obj.scale.y *= 2
obj.scale.z *= 0.1

#apply scale
bpy.ops.object.transform_apply()

# create variables for stacking and rotating
current_angle = 0
angle_step = 3
count = int(360 / angle_step)

# stack and rotate the mesh
for i in range(count):

    # duplicate the mesh
    bpy.ops.object.duplicate(linked=True)

    # get a reference to the currently active object
    dupObj = bpy.context.active_object
    
    # update the location of the object on the Z axis
    dupObj.location.z += dupObj.dimensions.z
    
    # update the angle for the next iteration
    current_angle += angle_step

    # update the rotation
    dupObj.rotation_euler.z = math.radians(current_angle)
