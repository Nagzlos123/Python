import numpy as np
import cv2
import sys

def zadanie():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

    image = cv2.imread('mask1.png', 1)
    if image is None:
        sys.exit(" Nie mozna wczytac obrazka mask.png")

    while True:
        cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            copy = image.copy()
            copy = cv2.resize(copy, (w, h))

            roi = frame[y:y + h, x:x + w]

            img2gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

            img2_fg = cv2.bitwise_and(copy, copy, mask=mask)

            dst = cv2.add(img1_bg, img2_fg)

            frame[y:y + h, x:x + w] = dst

        cv2.imshow('frame1', frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    zadanie()