import cv2

vid = cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    color = (0, 255,0 )
    stroke = 1

    for (x,y,w,h) in faces:
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
