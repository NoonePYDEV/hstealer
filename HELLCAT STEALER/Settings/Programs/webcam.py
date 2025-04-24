import cv2


try:
   webcam_capture = cv2.VideoCapture(0)
   ret, frame = webcam_capture.read()
   webcam_screenshot = cv2.imwrite(f"webcam.png", frame)
except:
   pass