import cv2
import numpy as np

def transform_img_to_rectangle(width, height, source_points, destination_pts):
    """
    Transforms the perspective of an image from a trapezoid to a rectangle.

    Parameters:
    - width: The width of the output image.
    - height: The height of the output image.
    - src_pts: A list of points defining the corners of the trapezoid in the input image.
    - dst_pts: A list of points defining the corners of the rectangle in the output image.
    """

    INPUT_PATH = '../input/boden.jpg'
    image = cv2.imread('../input/boden.jpg')
    
    if image is None:
        print(f"Error: Could not load image from {INPUT_PATH}")
        return

    # Calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(source_points, destination_pts)

    # Apply the perspective transformation
    transformed = cv2.warpPerspective(image, M, (width, height))
    cv2.imwrite('../output/wrappedimage.png',transformed)