import cv2
import numpy as np

# Load the image
image = cv2.imread('../input/boden.jpg')
width = 502
height = 743
# Specify the coordinates of the four corners of the trapezoid
# The order is: top-left, top-right, bottom-right, bottom-left
src_pts = np.array([[203, 66], [438, 76], [570, 396], [68, 396]], dtype="float32")

# Specify the coordinates of the rectangle you're transforming into
# This would typically be a straight rectangle, so we choose points accordingly
# The order should match the trapezoid's points: top-left, top-right, bottom-right, bottom-left
dst_pts = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype="float32")

# Calculate the perspective transform matrix
M = cv2.getPerspectiveTransform(src_pts, dst_pts)

# Apply the perspective transformation
transformed = cv2.warpPerspective(image, M, (width, height))
cv2.imwrite('../output/wrappedimage.png',transformed)