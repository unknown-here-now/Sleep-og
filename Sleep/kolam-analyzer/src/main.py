import cv2
import turtle
from image_processing import load_image, preprocess_image, detect_edges
from shape_detection import find_shapes, detect_dots

from kolam_turtle import setup_turtle, draw_shape

def main():
    image_path = input("Enter the path to the Kolam image: ")

    # Load and preprocess the image
    image = load_image(image_path)
    processed_image = preprocess_image(image)
    edges = detect_edges(processed_image)

    # Find shapes and dots
    shapes = find_shapes(edges)
    dots = detect_dots(processed_image)

    setup_turtle()

    # Draw detected shapes
    for shape_type, contour in shapes:
        draw_shape(shape_type, contour)

    # Draw detected dots
    for dot in dots:
        draw_shape("Dot", dot)

    turtle.done()

if __name__ == "__main__":
    main()