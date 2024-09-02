# give Python access to Blender's functionality
import bpy

# delete previously create object from last script run
bpy.ops.object.delete()

# add a cube into the scene
bpy.ops.mesh.primitive_cube_add()

# get a reference to the currently active objectcu
cube = bpy.context.active_object

# insert keyframe at frame one
start_frame = 1
cube.keyframe_insert("location",frame=start_frame)

# change the location of the cube on the x-axis, y-axis, and z-axis
cube.location = (-5,-5,-5)

# change the location of the cube on the z-axis
# cube.location.z = -5

# change the location of the cube on the x-axis
# cube.location.x = -5

# change the location of the cube on the y-axis
# cube.location.y = -5

# insert keyframe at mid frame
mid_frame = 90
cube.keyframe_insert("location",frame=mid_frame)

# change the location of the cube on the x-axis, y-axis, and z-axis
cube.location = (5,5,5)

# change the location of the cube on the z-axis
# cube.location.z = 5

# change the location of the cube on the x-axis
# cube.location.x = 5

# change the location of the cube on the y-axis
# cube.location.y = 5

# insert keyframe at the last frame
last_frame = 180
cube.keyframe_insert("location",frame=last_frame)
