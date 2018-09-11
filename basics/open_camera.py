import numpy as np
import cv2

# this allows for the video feature to start
cap = cv2.VideoCapture(0)

while True:
    # capture frame by frame
    ret, frame = cap.read()

    # flipping the frame for mirror effect 
    frame = cv2.flip(frame, 1)

    # operation on the frame -> grayscale transformation
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the resulting frame
    cv2.imshow('frame', frame)

    # if a key is pressed and that key is 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # break the loop
        break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
