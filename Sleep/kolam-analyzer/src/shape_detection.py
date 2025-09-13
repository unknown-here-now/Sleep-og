# shape_detection.py

import cv2
import numpy as np

def find_shapes(image):
    """Detects shapes in the given image and returns their contours and classifications."""
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    shapes = []

    for contour in contours:
        # Approximate the contour to reduce the number of points
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        shape_type = classify_shape(approx)
        shapes.append((shape_type, contour))

    return shapes

def classify_shape(approx):
    """Classifies the shape based on the number of vertices."""
    num_vertices = len(approx)

    if num_vertices == 3:
        return "Triangle"
    elif num_vertices == 4:
        # Check if it's a square or rectangle
        aspect_ratio = cv2.contourArea(approx) / (cv2.boundingRect(approx)[2] * cv2.boundingRect(approx)[3])
        return "Square" if aspect_ratio >= 0.95 else "Rectangle"
    elif num_vertices == 5:
        return "Pentagon"
    elif num_vertices == 6:
        return "Hexagon"
    elif num_vertices > 6:
        return "Circle"  # Assuming circular shapes for more than 6 vertices
    else:
        return "Unknown"

def detect_dots(image):
    """Detects dots in the image based on specific criteria."""
    # Thresholding to find bright spots (dots)
    _, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    dots = []

    for contour in contours:
        if cv2.contourArea(contour) < 50:  # Filter small contours
            dots.append(contour)

    return dots

def analyze_image(image_path):
    """Main function to analyze the image and detect shapes and dots."""
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 50, 150)

    shapes = find_shapes(edges)
    dots = detect_dots(gray_image)

    return shapes, dots