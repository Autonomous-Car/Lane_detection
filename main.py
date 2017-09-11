from lane_line import *
from config import *
from moviepy.editor import VideoFileClip
import os

if __name__ == '__main__':
    global SAVED_LB, SAVED_LT, SAVED_RB, SAVED_RT, ACTIVE
    SAVED_LB, SAVED_LT, SAVED_RB, SAVED_RT = None, None, None, None
    ACTIVE = False

    #input image
    img = cv2.imread()
    while True:
        result, signal = process_image(img)

        #print left, neutral right
        if signal == 0:
            text = "neutral"
        elif signal == -1:
            text = "left"
        elif signal == 1:
            text = "right"
        else: 
            text = "WARNING NO LANE DETECTED"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(result,text,(100,200), font, 1,(100,100,100),2)
        cv2.imshow("image",result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        rval, img = vc.read()
    vc.release()
    cv2.destroyAllWindows()