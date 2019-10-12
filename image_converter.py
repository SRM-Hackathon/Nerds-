import cv2 
import numpy as np 
import os
from os import walk

def converter(path , x_path):
    
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    l=[]
    for i in f:
        l.append( path + "/" + i )
    for i in range(len(l)):
        img = cv2.imread(l[i], 0) 
        kernel = np.ones((5,5), np.uint8) 
        img_erosion = cv2.erode(img, kernel, iterations=1) 
        cv2.imwrite(  os.path.join( x_path + str(i) + '.jpg' )  , img_erosion ) 
        cv2.waitKey(0)

path1  = "C:/Users/Shubham Gupta/Desktop/New folder (4)/old/test/nopothole"
path10 = 'C:/Users/Shubham Gupta/Desktop/New folder (4)/new/test/nopothole'

path2  = "C:/Users/Shubham Gupta/Desktop/New folder (4)/old/test/pothole"
path20 = 'C:/Users/Shubham Gupta/Desktop/New folder (4)/new/test/pothole'

path3  = "C:/Users/Shubham Gupta/Desktop/New folder (4)/old/train/nopothole"
path30 = 'C:/Users/Shubham Gupta/Desktop/New folder (4)/new/train/nopothole'

path4  = "C:/Users/Shubham Gupta/Desktop/New folder (4)/old/train/pothole"
path40 = 'C:/Users/Shubham Gupta/Desktop/New folder (4)/new/train/pothole'


converter(path1 , path10)
converter(path2 , path20)
converter(path3 , path30)
converter(path4 , path40)

