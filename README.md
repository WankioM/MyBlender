# MyBlender
Recreating steps addon but edited from the source code
1. Download the ZIP file of this addon
2. Open Blender
3. Go to Edit > Preferences
4. Select the "Add-ons" tab
5. Click "Install..." and browse to the downloaded ZIP file
6. Enable the addon by checking the box next to "3D View: Quick Blender Addon"

## Usage

1. Open the sidebar in the 3D View by pressing `N`
2. Look for the "Quick Tools" tab
3. Use the provided tools:
   - **Cube Array**: Creates multiple cubes in a row with adjustable count and spacing
   - **Smooth Selected**: Applies smooth shading with auto-smooth enabled to selected objects

## Files Structure

- `__init__.py`: Main addon file with registration functions
- `operators.py`: Contains the operators that provide the addon functionality
- `panel.py`: Creates the UI panel in the sidebar

## Requirements

- Blender 3.0.0 or newer

## License

This addon is released under the MIT License.