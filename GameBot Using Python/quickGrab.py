from PIL import ImageGrab   # to grab image
import os
import time

def screenGrab():
    # B_box = (x,y,x,y)
    x=345
    y=280
   # x1=1140
   # y1=860
    im = ImageGrab.grab((x,y,x+795,y+585))
    im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png','PNG')
    
if __name__=='__main__':
    screenGrab()