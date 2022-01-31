import cv2
import winsound
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(r'\mask_detection.xml')
count = 0
while True:
	ret, frame = video.read()
	faces = facedetect.detectMultiScale(frame, 1.3, 5)
	for x, y, w, h in faces:
		count = count + 1
		winsound.PlaySound(r'\alert.wav', winsound.SND_ASYNC)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

		cv2.putText(frame, "No Mask", (x+15 , y-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (0, 0, 255), 1)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
video.release()
cv2.destroyAllWindows()
