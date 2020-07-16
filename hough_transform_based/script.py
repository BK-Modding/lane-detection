import os
import re
import cv2
import numpy as np
from tqdm import tqdm_notebook
import matplotlib.pyplot as plt

VIDEO_PATH = "drivingvideo.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(width), int(height)))

frame_list = []

count = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        frame = np.asarray(frame)
        # results = tfnet.return_predict(frame)

        frame_list.append(frame)

        if count > 5:
            break

        count += 1

        new_frame = frame

        # Display the resulting frame
        # out.write(new_frame)
        # cv2.imshow('frame', new_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

disp_frame = frame_list[0]

plt.figure(figsize=(10,10))
plt.imshow(disp_frame[:,:,0], cmap= "gray")
plt.show()

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
