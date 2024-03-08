import cv2
import numpy as np

from transform import *

def main():
    width = 502
    height = 743
    #src_pts = detect_rectangle_edges()
    # if src_pts is None:
    #     print("Could not detect rectangle edges.")
    #     return
    
    #top-left, top-right, bottom-right, bottom-left
    #test = np.float32([[203,67],[435,77],[566,388],[70,394]])
    
    #src_pts = np.array(src_pts, dtype=np.float32)  # Ensure src_pts is correctly formatted
    src_pts = np.array(detect_rectangle_edges(), dtype=np.float32)
    dst_pts = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
    transform_img_to_rectangle(width, height, src_pts, dst_pts)
    
    
    
    
    #src_pts = np.array(src_pts, dtype=np.float32)  # Ensure src_pts is correctly formatted


if __name__ == "__main__":
    main()
    
    