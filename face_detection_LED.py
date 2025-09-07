import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

arduino = SerialObject("/dev/cu.usbmodem11301",9600)

cap = cv2.VideoCapture(0)

detector = FaceDetector(0.8)

while True:
    success, img = cap.read()
    img, bboxs =  detector.findFaces(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if bboxs:
        arduino.sendData([0,1,0])
    else:
        arduino.sendData([1,0,0])
    