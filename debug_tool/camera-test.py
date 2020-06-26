import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera', frame)
    if cv2.waitKey(1)==27: # ESCで抜ける
        break
cap.release()
cv2.destroyAllWindows()
