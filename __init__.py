import bpy
from . import operators
from . import panel

bl_info = {
    "name": "Quick Blender Addon",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Quick Tools",
    "description": "A quick addon with simple tools",
    "category": "3D View",
}

def register():
    operators.register()
    panel.register()

def unregister():
    panel.unregister()
    operators.unregister()

if __name__ == "__main__":
    register()