import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)

video = cv2.VideoCapture(1)  # --> Switch webcam

while True:
    ret, frame = video.read()
    hands, img = detector.findHands(frame)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.relase()
cv2.destroyAllWindows()
