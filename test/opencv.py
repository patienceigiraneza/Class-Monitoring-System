import cv2
import time
vid = cv2.VideoCapture('rtsp://iot:ida-12345@192.168.1.91:554/Streaming/Channels/1/')

re_try = True
while re_try:
	try:
		ret, frame = vid.read()
		cv2.imshow('frame', frame)
		re_try = False
	except:
		time.sleep(1)
		print("Not yet")


while vid.isOpened():
	ret, frame = vid.read()
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
