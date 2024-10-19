import numpy as np
import cv2
def zadanie():

    cap = cv2.VideoCapture(0)

    lastframe = None

    while True:
        cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)

        ret, frame = cap.read()

        diff = None
        if lastframe is not None:
            diff = cv2.absdiff(frame, lastframe)
            ret, thresh1 = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            dilation = cv2.erode(thresh1, np.ones((5, 5), np.uint8), iterations=1)
            gray = cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)

            # check OpenCV version

            contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            min = [frame.shape[1], 0, 0, frame.shape[0]]
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if x < min[0]: min[0] = x
                if y > min[1]: min[1] = y
                if x + w > min[2]: min[2] = x
                if y + h < min[3]: min[3] = y
            cv2.rectangle(frame, tuple(min[:2]), tuple(min[2:]), (0, 255, 0), 2)

        cv2.imshow('frame1', frame)

        lastframe = frame

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    zadanie()