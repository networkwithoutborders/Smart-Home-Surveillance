import cv2
import imutils
import numpy as np

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

capture = cv2.VideoCapture(0)
firstFrame = None
while (True):
    ret, frame = capture.read()
    if frame is None:
        break
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4),
                                                              padding=(4, 4),
                                                              scale=1.05)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        if len(weights) == 1 and weights[0][0] > 0.3:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()