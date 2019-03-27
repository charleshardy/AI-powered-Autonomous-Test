#!/usr/bin/env python3
# USAGE
# python ocr.py
import cv2
import sys
import pytesseract
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
cap.set(3, 1280) # set the Horizontal resolution
cap.set(4, 720) # Set the Vertical resolution

config = ('-l eng --oem 1 --psm 3')

substring = "end trace"

#font = cv2.FONT_HERSHEY_SIMPLEX
font = cv2.FONT_HERSHEY_DUPLEX
 
while(cap.isOpened()):
  ret,frame = cap.read()
  #gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
  cv2.imshow('Kernel Call trace Detect',frame)

  #text = pytesseract.image_to_string(gray, config=config)
  text = pytesseract.image_to_string(frame, config=config)
  if text.find(substring) is not -1:
    cv2.putText(frame,'Call trace detected!',(50,300), font, 4, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow('Kernel Call Trace Detect',frame)
    start_time = time.time()
    while True:
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      waited = time.time() - start_time
      if waited >= 5:
        break
    print("Call trace detected!")
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
