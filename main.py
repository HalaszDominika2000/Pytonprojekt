from dolgozok import * # * minden látszik

def menu():
    print("--- Dolgozókezelő Program ---")
    print("1. Dolgozó felvétele")
    print("2. Dolgozó törlése")
    print("3. Dolgozó adatainak módosítása")
    print("4. Összes fizetés kiszámítása")
    print("5. Véletlenszerű 'legmagasabb fizetésű' dolgozó")
    print("6. Véletlenszerű 'legalacsonyabb fizetésű' dolgozó")
    print("7. Dolgozók listázása (fizetés szerint rendezve)")
    print("0. Kilépés")

def main():
    dolgozok = adatokat_betolt()


    fut = True
    while fut:
        menu()
        valaszt = input("Válassz egy opciót: ")


        if valaszt == "1":
            dolgozo_hozzaad(dolgozok)


        elif valaszt == "2":
            dolgozo_torol(dolgozok)


        elif valaszt == "3":
            dolgozo_modosit(dolgozok)


        elif valaszt == "4":
            print("Összes fizetés:", fizetes_osszeg(dolgozok), "Ft")


        elif valaszt == "5":
            d = legmagasabb_fizetes(dolgozok)
            if d:
                print("Legmagasabb fizetésű (véletlenszerű):", d.nev, d.fizetes, "Ft")
            else:
                print("Nincs adat!")


        elif valaszt == "6":
            d = legalacsonyabb_fizetes(dolgozok)
            if d:
                print("Legalacsonyabb fizetésű (véletlenszerű):", d.nev, d.fizetes, "Ft")
            else:
                print("Nincs adat!")


        elif valaszt == "7":
            lista = rendezes_fizetes_szerint(dolgozok)
            for d in lista:
                print(d.nev, "-", d.fizetes, "Ft")


        elif valaszt == "0":
            print("Kilépés...")
            fut = False


        else:
            print("Érvénytelen választás!")


        adatokat_ment(dolgozok)




if __name__ == "__main__":
    main()