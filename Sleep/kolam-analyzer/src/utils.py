def choose_color(shape_type):
    """Selects a color based on the shape type."""
    color_map = {
        'hexagon': 'blue',
        'petal': 'red',
        'diamond': 'green',
        'dot': 'yellow'
    }
    return color_map.get(shape_type, 'black')  # Default to black if shape type is unknown

def set_line_thickness(thickness):
    """Sets the line thickness for drawing shapes."""
    if thickness < 1:
        thickness = 1  # Minimum thickness
    return thickness