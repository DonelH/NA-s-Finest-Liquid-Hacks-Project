# Controller -- Mediator between View & Model including flask

import numpy as np
import cv2

## Capturing the Video

capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read() # Capture frames
    
    cv2.imshow('Camera View', frame) # Display the given frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
capture.release()
cv2.destroyAllWindows()

