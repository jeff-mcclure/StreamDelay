# -*- coding: utf-8 -*-
"""
Screen capture delay, quit by pressing the q key
"""
import cv2
import numpy as np
from PIL import ImageGrab

WINDOW_EXT = (100, 100, 1220, 780)
DELAY = 1000

# Fill the image buffer for delay duration.
buffer = []
for i in range(DELAY):
    img = ImageGrab.grab(bbox=WINDOW_EXT) #x, y, w, h
    RGB_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    buffer.append(RGB_img)
    if cv2.waitKey(1) == ord('q'):
        break

# Continuosly push to buffer and pop image from bottom of the stack for display.
while True:
    img = ImageGrab.grab(bbox=WINDOW_EXT) #x, y, w, h
    RGB_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    buffer.append(RGB_img)
    
    cv2.imshow('Delayed Window', buffer.pop(0))
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()