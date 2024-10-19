import numpy as np
import cv2
def lab3():
    cap = cv2.VideoCapture(0)

    while True:
        cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
        cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)

        ret, frame = cap.read()

        kernel = np.ones((17, 17), np.uint8)
        kernel2 = np.ones((3, 3), np.uint8)

        erosion = cv2.erode(frame, kernel, iterations=1)
        dilation = cv2.dilate(frame, kernel, iterations=1)
        inv = cv2.cvtColor(255 - cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
        gradient = cv2.cvtColor(cv2.morphologyEx(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.MORPH_GRADIENT, kernel2),
                                cv2.COLOR_GRAY2BGR)

        endframe = np.hstack((frame, erosion, dilation, inv, gradient))

        cv2.imshow('frame1', endframe)

        mirror1 = frame[::1, ::-1]
        mirror2 = frame[::-1, ::1]
        mirror3 = frame[::-1, ::-1]

        cv2.imshow('frame2', np.vstack((np.hstack((frame, mirror1)), np.hstack((mirror2, mirror3)))))

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    lab3()