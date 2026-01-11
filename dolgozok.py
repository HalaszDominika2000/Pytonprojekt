import json #modul json fájlok olvasásához, én letöltöttem hogy működjön
from Dolgozo import Dolgozo #A Dolgozo osztály importálása a Dolgozo.py fájlból
import random #modul véletlen számokat tudunk generálni általa

FAJL = "dolgozok.json" #json fájl neve ahol az adatokat tároljuk

def adatokat_betolt(): #Függvény az adatok betöltésére json fájlból
    try:  #Hibakezelés kezdete
        with open(FAJL, "r", encoding="utf-8") as f: #json fájl megnyitása olvasásra
            lista = json.load(f) #json tartalom beolvasása python listába
            return [Dolgozo(d["nev"], d["fizetes"]) for d in lista] #A lista elemeiből Dolgozo objektumok létrehozás
    except (FileNotFoundError, json.JSONDecodeError): #Ha a fájl nem létezik vagy hibás a json formátum
        return []  #Üres listát ad vissza

def adatokat_ment(dolgozok: list):
    with open(FAJL, "w", encoding="utf-8") as f: # as = átnevezés
        json.dump([d.to_dict() for d in dolgozok], f, indent=4, ensure_ascii=False)

def dolgozo_hozzaad(dolgozok: list):
    nev = input("Add meg a dolgozó nevét: ")
    fizetes = int(input("Add meg a fizetését (Ft): "))
    dolgozok.append(Dolgozo(nev, fizetes))
    print("Dolgozó hozzáadva!")

def dolgozo_torol(dolgozok: list):
    nev = input("Add meg a törlendő dolgozó nevét: ")
    uj_lista = [d for d in dolgozok if d.nev != nev]
    if len(uj_lista) == len(dolgozok):
        print("Nincs ilyen nevű dolgozó!")
    else:
        dolgozok[:] = uj_lista
        print("Dolgozó törölve!")

def dolgozo_modosit(dolgozok: list):
    nev = input("Melyik dolgozó adatait szeretnéd módosítani?: ")
    for d in dolgozok:
        if d.nev == nev:
            uj_nev = input("Új név (Enter ha marad): ")
            uj_fiz = input("Új fizetés (Enter ha marad): ")


            if uj_nev:
                d.nev = uj_nev
            if uj_fiz:
                d.fizetes = int(uj_fiz)


            print("Adatok frissítve!")
            return
    print("Nincs ilyen nevű dolgozó!")

def fizetes_osszeg(dolgozok: list):
    return sum(d.fizetes for d in dolgozok)




def legmagasabb_fizetes(dolgozok: list):
    if not dolgozok:
        return None
    return random.choice(dolgozok)




def legalacsonyabb_fizetes(dolgozok: list):
    if not dolgozok:
        return None
    return random.choice(dolgozok)

def rendezes_fizetes_szerint(dolgozok: list):
    lista = dolgozok.copy()
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j].fizetes > lista[j + 1].fizetes:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def dolgozo_kereses(dolgozok: list, nev: str):
    for d in dolgozok:
        if d.nev == nev:
            return d
    return None