import sys

import cv2
import numpy as np
def zadanie1():
    # Stworzenie obrazu
    empty = np.zeros((1000, 1000), np.uint8)

    # Konwersja na BGR
    color = cv2.cvtColor(empty, cv2.COLOR_RGB2BGR)

    # Kolo
    cv2.circle(color, (500, 500), 450, (0, 0, 255), 8)
    cv2.circle(color, (500, 500), 400, (0, 255, 0), 16)
    cv2.circle(color, (500, 500), 350, (0, 0, 255), 8)
    cv2.circle(color, (500, 500), 300, (0, 255, 0), 16)
    cv2.circle(color, (500, 500), 250, (255, 0, 0), 8)
    cv2.circle(color, (500, 500), 200, (255, 0, 0), 16)
    cv2.circle(color, (500, 500), 250, (255, 0, 0), 20)
    cv2.circle(color, (500, 500), 200, (255, 0, 0), 20)
    cv2.circle(color, (500, 500), 150, (0, 0, 255), 20)
    cv2.circle(color, (500, 500), 100, (0, 255, 0), 20)
    # Wyswietlenie
    cv2.namedWindow('Zadanie 1', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 1', color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def zadanie2():
    # Wczytanie obrazka
    img = cv2.imread("glowa.png", -1)
    if img is None:
        sys.exit(" Nie mozna wczytac obrazka ")

    # Wyswietlenie
    cv2.namedWindow('Zadanie 2', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Zadanie 2', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie3():
    # Wczytanie obrazka w skali szarosci
    img = cv2.imread("glowa.png", 0)
    if img is None:
        sys.exit(" Nie mozna wczytac obrazka ")

    # 1. Rozmazanie
    blur = cv2.blur(img, (5, 5))

    # 2. Erozja
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(blur, kernel, iterations=1)

    # 3. Gradient morfologiczny
    gradient = cv2.morphologyEx(erosion, cv2.MORPH_GRADIENT, kernel)

    # 4. Inwersja
    inv = 255 - gradient

    # Pusty obraz dla wypelnienia
    empty = np.empty(img.shape, np.uint8)

    # Wyswietlenie
    cv2.namedWindow('Zadanie 3', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 3', np.vstack((
        np.hstack((img, blur)),
        np.hstack((erosion, gradient)),
        np.hstack((inv, empty))
    )))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zadanie4():
    # Wczytanie obrazka
    img = cv2.imread("glowa.png", 1)
    if img is None:
        sys.exit(" Nie mozna wczytac obrazka ")


    # Odbicia
    mirror1 = img[::1, ::-1]
    mirror2 = img[::-1, ::1]
    mirror3 = img[::-1, ::-1]

    # Dodanie ramek do obrazow
    borderSize = 3

    img = cv2.copyMakeBorder(img, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_CONSTANT)
    mirror1 = cv2.copyMakeBorder(mirror1, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_CONSTANT)
    mirror2 = cv2.copyMakeBorder(mirror2, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_CONSTANT)
    mirror3 = cv2.copyMakeBorder(mirror3, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_CONSTANT)

    # Wyswietlenie
    cv2.namedWindow('Zadanie 4', cv2.WINDOW_NORMAL)
    cv2.imshow('Zadanie 4', np.vstack((np.hstack((img, mirror1)), np.hstack((mirror2, mirror3)))))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
