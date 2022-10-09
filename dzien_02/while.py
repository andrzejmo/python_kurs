import random

DEBUG = True

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

ruch_counter = 0

odleglosc_poczatkowa = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

while True:

    print(f"Pozycja gracza: {gracz_x=} {gracz_y=}")

    odleglosc_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    polecenie = input("Wykonaj ruch (w-gora, a-lewo, s-doł, d-prawo): ")

    # if polecenie == "w" or polecenie == "s" or polecenie == "a" or polecenie == "d":
    #     ruch_counter += 1

    if polecenie in "wasd" and len(polecenie) == 1:
        ruch_counter += 1

    if polecenie == "w":
        gracz_y += 1
    elif polecenie == "s":
        gracz_y -= 1
    elif polecenie == "a":
        gracz_x -= 1
    elif polecenie == "d":
        gracz_x += 1
    else:
        print("Nie o co Ci chodzi!")


    if gracz_y == skarb_y and gracz_x == skarb_x:
        print(f"Znalazłeś skarb po {ruch_counter} ruchach!")
        break

    if gracz_y > 10 or gracz_x > 10 or gracz_x < 0 or gracz_y < 0:
        print("Wypadłeś poza planszę")
        break

    if ruch_counter > 2 * odleglosc_poczatkowa:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        ruch_counter = 0
        odleglosc_poczatkowa = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        print("Za długo błądzisz - skarb zmienił położenie")
        continue


    odleglosc_po = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    if random.randint(1, 5) != 2:
        if odleglosc_po < odleglosc_przed:
            print("Ciepło")
        elif odleglosc_po > odleglosc_przed:
            print("Zimno")
    else:
        print(" A nie powiem !!!")

    if DEBUG:
        print(f"Pozycja skarbu: {skarb_x=} {skarb_y=}")


