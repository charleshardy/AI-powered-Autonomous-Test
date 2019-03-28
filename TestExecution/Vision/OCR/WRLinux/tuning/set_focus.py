#!/usr/bin/env python3
# USAGE
# python ocr.py
import cv2
import sys
import pytesseract


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
cap.set(3, 1280) # set the Horizontal resolution
cap.set(4, 720) # Set the Vertical resolution

#config = ('-l eng --oem 1 --psm 3')
#cap.set(cv2.CAP_PROP_FOCUS,10)
#cap.set(cv2.CAP_PROP_ZOOM,10)
#cap.set(cv2.CAP_PROP_BRIGHTNESS,50)
#cap.set(cv2.CAP_PROP_CONTRAST,50)
#cap.set(cv2.CAP_PROP_SATURATION,50)
#cap.set(cv2.CAP_PROP_HUE,50)
#cap.set(cv2.CAP_PROP_EXPOSURE,50)
#cap.set(cv2.CAP_PROP_EXPOSURE,25)

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

config = ('-l eng --oem 1 --psm 3')

substring = "end trace"
 
while(cap.isOpened()):
  ret,frame = cap.read()
  gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',frame)
#  text = pytesseract.image_to_string(frame, config=config)
  text = pytesseract.image_to_string(gray, config=config)
  if text.find(substring) is not -1:
    print("Call trace detected!")
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
