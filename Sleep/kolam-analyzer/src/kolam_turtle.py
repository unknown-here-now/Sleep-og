import turtle

def setup_turtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

def draw_shape(shape_type, contour):
    # Get the points from the contour
    points = [pt[0] for pt in contour]

    if shape_type == "Dot":
        if points:
            x, y = points[0]
            turtle.penup()
            turtle.goto(x - 250, 250 - y)
            turtle.pendown()
            turtle.dot(8, "red")
    else:
        if points:
            turtle.penup()
            x, y = points[0]
            turtle.goto(x - 250, 250 - y)
            turtle.pendown()
            turtle.pensize(2)
            turtle.color("black")
            for pt in points[1:]:
                x, y = pt
                turtle.goto(x - 250, 250 - y)
            # Close the shape
            x, y = points[0]
            turtle.goto(x - 250, 250 - y)
            turtle.penup()