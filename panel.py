def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    # Register properties
    bpy.types.Scene.qt_cube_count = bpy.props.IntProperty(
        name="Count",
        description="Number of cubes",
        default=3,
        min=1,
        max=20
    )
    
    bpy.types.Scene.qt_cube_spacing = bpy.props.FloatProperty(
        name="Spacing",
        description="Distance between cubes",
        default=2.0,
        min=0.0,
        soft_max=10.0
    )

def unregister():
    # Unregister properties
    del bpy.types.Scene.qt_cube_count
    del bpy.types.Scene.qt_cube_spacing
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)