import cv2
import numpy as np

from transform import detect_rectangle_edges, transform_img_to_rectangle
def main():
    width = 502
    height = 743
    src_pts = detect_rectangle_edges()
    if src_pts is None:
        print("Could not detect rectangle edges.")
        return
    #src_pts = np.array(src_pts, dtype=np.float32)  # Ensure src_pts is correctly formatted
    src_pts = np.array(detect_rectangle_edges(), dtype=np.float32)
    dst_pts = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype=np.float32)
    transform_img_to_rectangle(width, height, src_pts, dst_pts)
    
    src_pts = detect_rectangle_edges()
    if src_pts is None:
        print("Could not detect rectangle edges.")
        return
    src_pts = np.array(src_pts, dtype=np.float32)  # Ensure src_pts is correctly formatted
    # Existing setup code...
    
    # Proceed with transformation...


if __name__ == "__main__":
    main()