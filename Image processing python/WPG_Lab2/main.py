import cv2
import numpy as np
import sys

img1 = cv2.imread("elementy1.png", 0)

if img1 is None:
    sys.exit(" Nie mozna wczytac obrazka elementy1.png")

img2 = cv2.imread("elementy2.png", 0)

if img2 is None:
    sys.exit(" Nie mozna wczytac obrazka elementy2.png")

background = cv2.imread("tlo.png", 1)

if background is None:
    sys.exit(" Nie mozna wczytac obrazka tlo.png")

background2 = cv2.imread("tlo_z.png", 1)

if background2 is None:
    sys.exit(" Nie mozna wczytac obrazka tlo_z.png")

hsep = np.full((img1.shape[0], 5), 127, np.uint8)
hsep2 = np.full((background.shape[0], 5), 127, np.uint8)
def przyklad11():

    add1 = img1 + img2
    sub1 = img1 - img2
    mul1 = img1 * img2
    and1 = img1 & img2
    or1 = img1 | img2
    not1 = 255 - img1

    cv2.namedWindow('Zadanie 1 - Przyklad 1:', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 1 - Przyklad 1:', np.vstack((
        np.hstack((img1, hsep, img2)),
        np.full((5, np.hstack((img1, hsep, img2)).shape[1]), 127, np.uint8),
        np.hstack((add1, hsep, sub1)),
        np.full((5, np.hstack((img1, hsep, img2)).shape[1]), 127, np.uint8),
        np.hstack((mul1, hsep, and1)),
        np.full((5, np.hstack((img1, hsep, img2)).shape[1]), 127, np.uint8),
        np.hstack((or1, hsep, not1))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def przyklad12():
    add2 = img1 + img1
    sub2 = img1 - img1
    mul2 = img1 * img1
    and2 = img1 & img1
    or2 = img1 | img1
    not2 = 255 - img1

    cv2.namedWindow('Zadanie 1 - Przyklad 2:', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 1 - Przyklad 2:', np.vstack((
        np.hstack((img1, hsep, img1)),
        np.full((5, np.hstack((img1, hsep, img1)).shape[1]), 127, np.uint8),
        np.hstack((add2, hsep, sub2)),
        np.full((5, np.hstack((img1, hsep, img1)).shape[1]), 127, np.uint8),
        np.hstack((mul2, hsep, and2)),
        np.full((5, np.hstack((img1, hsep, img1)).shape[1]), 127, np.uint8),
        np.hstack((or2, hsep, not2))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def przyklad13():

    add3 = background + background
    sub3 = background - background
    mul3 = background * background
    and3 = background & background
    or3 = background | background
    not3 = 255 - background

    cv2.namedWindow('Zadanie 1 - Przyklad 3:', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 1 - Przyklad 3:', np.vstack((
        np.hstack((background, background)),
        np.hstack((add3, sub3)),
        np.hstack((mul3, and3)),
        np.hstack((or3, not3))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def przyklad14():
    add4 = background + background2
    sub4 = background - background2
    mul4 = background * background2
    and4 = background & background2
    or4 = background | background2
    not4 = 255 - background

    cv2.namedWindow('Zadanie 1 - Przyklad 4:', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 1 - Przyklad 4:', np.vstack((
        np.hstack((background, background2)),
        np.hstack((add4, sub4)),
        np.hstack((mul4, and4)),
        np.hstack((or4, not4))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def przyklad21():
    kernel = np.ones((5, 5), np.uint8)

    erosion1 = cv2.erode(img1, kernel, iterations=1)
    dilation1 = cv2.dilate(img1, kernel, iterations=1)
    opening1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

    empty1 = np.zeros(img1.shape, np.uint8)

    cv2.namedWindow('Zadanie 2 - Przyklad 1:', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 2 - Przyklad 1:', np.vstack((
        np.hstack((img1, empty1)),
        np.hstack((erosion1, dilation1)),
        np.hstack((opening1, closing1))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def przyklad22():
    kernel = np.ones((7, 7), np.uint8)

    erosion2 = cv2.erode(background, kernel, iterations=1)
    dilation2 = cv2.dilate(background, kernel, iterations=1)
    opening2 = cv2.morphologyEx(background, cv2.MORPH_OPEN, kernel)
    closing2 = cv2.morphologyEx(background, cv2.MORPH_CLOSE, kernel)

    empty2 = np.zeros(background.shape, np.uint8)

    cv2.namedWindow('Zadanie 2 - Przyklad 2:', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 2 - Przyklad 2:', np.vstack((
        np.hstack((background, empty2)),
        np.hstack((erosion2, dilation2)),
        np.hstack((opening2, closing2))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zadanie1():
    przyklad11()
    przyklad12()
    przyklad13()
    przyklad14()

def zadanie2():

    przyklad21()
    przyklad22()


if __name__ == "__main__":
    zadanie1()
    zadanie2()