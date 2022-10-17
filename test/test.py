import cv2
vid = cv2.VideoCapture(0)

while True:

    ret, frame1 = vid.read()
    ret, frame2 = vid.read()
    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)


    cv2.imshow('frame', blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
