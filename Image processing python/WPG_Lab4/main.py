import numpy as np
import cv2
import sys
def zadanie():
    cap = cv2.VideoCapture(0)

    marker1 = cv2.imread("marker1.png", 0);
    if marker1 is None:
        sys.exit(" Nie mozna wczytac obrazka marker1")

    marker2 = cv2.imread("marker2.png", 0);
    if marker2 is None:
        sys.exit(" Nie mozna wczytac obrazka marker2")

    markers = [marker1, marker2]

    while True:
        cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)

        ret, frame = cap.read()

        imggray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(imggray)

        for m in markers:
            res = cv2.matchTemplate(gray, m, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                w, h = m.shape[::-1]
                cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv2.imshow('frame1', frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    zadanie()
