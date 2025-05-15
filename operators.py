import bpy
import bmesh
from bpy.types import Operator
from bpy.props import FloatProperty, IntProperty

class QUICKTOOLS_OT_add_cube_array(Operator):
    """Add a linear array of cubes"""
    bl_idname = "quicktools.add_cube_array"
    bl_label = "Add Cube Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    count: IntProperty(
        name="Count",
        description="Number of cubes",
        default=3,
        min=1,
        max=20
    )
    
    spacing: FloatProperty(
        name="Spacing",
        description="Distance between cubes",
        default=2.0,
        min=0.0,
        soft_max=10.0
    )
    
    def execute(self, context):
        for i in range(self.count):
            bpy.ops.mesh.primitive_cube_add(location=(i * self.spacing, 0, 0))
            
        return {'FINISHED'}


class QUICKTOOLS_OT_smooth_selected(Operator):
    """Apply smooth shading to selected objects"""
    bl_idname = "quicktools.smooth_selected"
    bl_label = "Smooth Selected"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'CANCELLED'}
            
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                # Set smooth shading
                bpy.ops.object.shade_smooth()
                
                # Enable auto smooth
                if obj.data:
                    obj.data.use_auto_smooth = True
                    obj.data.auto_smooth_angle = 0.523599  # 30 degrees
                
        return {'FINISHED'}


# List of all classes to register
classes = (
    QUICKTOOLS_OT_add_cube_array,
    QUICKTOOLS_OT_smooth_selected,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)