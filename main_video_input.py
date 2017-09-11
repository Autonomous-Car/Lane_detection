from lane_line import *
from config import *
from moviepy.editor import VideoFileClip
import os

if __name__ == '__main__':
    global SAVED_LB, SAVED_LT, SAVED_RB, SAVED_RT, ACTIVE
    SAVED_LB, SAVED_LT, SAVED_RB, SAVED_RT = None, None, None, None
    ACTIVE = False

    #vc = cv2.VideoCapture(os.getcwd()+"/source/input2.mp4")
    vc = cv2.VideoCapture(0)
    if vc.isOpened():
        rval , img = vc.read()
    else:
        rval = False

    while rval:
        result, signal = process_image(img)
        #print left, neutral right
        if signal == 0:
            text = "neutral"
            rect = [(90, 170), (235, 210)]
        elif signal == -1:
            text = "left"
            rect = [(90, 170), (165, 210)]
        elif signal == 1:
            text = "right"
            rect = [(90, 170), (195, 210)]
        else: 
            text = "WARNING NO LANE DETECTED"
            rect = [(90, 170), (600, 210)]
        font = cv2.FONT_HERSHEY_COMPLEX 
        cv2.putText(result,text,(100,200), font, 1,(0, 0, 255),2)
        cv2.rectangle(result, rect[0], rect[1], (0, 0, 255), 2)
        cv2.imshow("image",result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        rval, img = vc.read()
    vc.release()
    cv2.destroyAllWindows()