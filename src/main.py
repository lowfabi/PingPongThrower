import cv2
import numpy as np

from transform import transform_img_to_rectangle

def main():
    width = 502
    height = 743
    src_pts = np.array([[203, 66], [438, 76], [570, 396], [68, 396]], dtype="float32")
    dst_pts = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype="float32")
    transform_img_to_rectangle(width, height, src_pts, dst_pts)

if __name__ == "__main__":
    main()
