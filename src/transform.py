import cv2
import numpy as np

INPUT_PATH = '../input/boden.jpg'

def transform_img_to_rectangle(width, height, source_points, destination_pts):
    """
    Transforms the perspective of an image from a trapezoid to a rectangle.

    Parameters:
    - width: The width of the output image.
    - height: The height of the output image.
    - src_pts: A list of points defining the corners of the trapezoid in the input image.
    - dst_pts: A list of points defining the corners of the rectangle in the output image.
    """

    image = cv2.imread(INPUT_PATH)
    
    if image is None:
        print(f"Error: Could not load image from {INPUT_PATH}")
        return

    # Calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(source_points, destination_pts)

    # Apply the perspective transformation
    transformed = cv2.warpPerspective(image, M, (width, height))
    cv2.imwrite('../output/wrappedimage5.png',transformed)
    
def px_to_cm(x,y):
    np.array([x/4,y/4])
    
def detect_rectangle_edges():
    # Load the image
    image = cv2.imread(INPUT_PATH)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and approximate them
    for contour in contours:
        # Approximate the contour
        perimeter = cv2.arcLength(contour, True)
        approximation = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # Check if the approximated contour has four points
        if len(approximation) == 4:
            # These points are the corners of the rectangle
            corners = approximation.reshape(4, 2)
            print("Rectangle corners:", corners)
            
            # Optional: draw the rectangle on the image
            cv2.drawContours(image, [approximation], -1, (0, 255, 0), 3)
            cv2.imshow('Rectangle Detected', image)
            cv2.waitKey(0)
            break
            return corners
