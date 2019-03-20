import cv2
import sys
import pytesseract

cap = cv2.VideoCapture(0)

config = ('-l eng --oem 1 --psm 3')

while(cap.isOpened()):
  ret,frame = cap.read()
  cv2.imshow('frame',frame)
  text = pytesseract.image_to_string(frame, config=config)
  if text:
    print(text)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
