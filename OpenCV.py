import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   1, # min
                   10, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):

    ret, frame = cap.read()
    if not ret: continue


    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

     
    #カラーを変更
    def color(x):
        if(v==0):
            y = frame
        elif(v==1):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
        elif (v==2):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        elif (v==3):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2XYZ)
        elif (v==4):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2YCrCb)
        elif (v==5):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2HSV)
        elif (v==6):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2Lab)
        elif (v==7):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2HLS)
        elif (v==8):
            y = cv2.cvtColor(x, cv2.COLOR_BGR2YUV)
        else:
            y = frame
            
        return y
        
    #コントラスト変更
    def contrast(x):
        M = 128
        if(v==0):
            y = frame
        else:
            y = 1/(1 + (M/(frame+0.01))**v)
            y = y * 255
            y = y.astype(np.uint8)
        
        return y
    
    #フィルタリング
    def filtering(x):
        if(v==0):
            average_square=(1,1)
        else:
            average_square=(v*2+1, v*2+1)
        y = cv2.blur(frame, average_square)
        
        return y
    
    cv2.imshow('title', filtering(frame) ) # show in the win
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
