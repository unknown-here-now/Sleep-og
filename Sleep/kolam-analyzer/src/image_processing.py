# Contents of /kolam-analyzer/kolam-analyzer/src/image_processing.py

import cv2
import numpy as np

def load_image(image_path):
    """
    Load an image from the specified file path.
    
    Parameters:
    image_path (str): The path to the image file.
    
    Returns:
    numpy.ndarray: The loaded image.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return image

def preprocess_image(image):
    """
    Convert the image to grayscale and apply Gaussian blur.
    
    Parameters:
    image (numpy.ndarray): The input image.
    
    Returns:
    numpy.ndarray: The preprocessed image.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    return blurred_image

def detect_edges(image):
    """
    Apply Canny edge detection to the image.
    
    Parameters:
    image (numpy.ndarray): The input image.
    
    Returns:
    numpy.ndarray: The edges detected in the image.
    """
    edges = cv2.Canny(image, 100, 200)
    return edges