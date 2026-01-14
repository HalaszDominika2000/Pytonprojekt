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

def adatokat_ment(dolgozok: list): #Függvény a dolgozók adatainak mentésére
    with open(FAJL, "w", encoding="utf-8") as f: # as = átnevezés Fájl megnyitása írásra 
        json.dump([d.to_dict() for d in dolgozok], f, indent=4, ensure_ascii=False)
        #A dolgozók listáját JSON formátumban fájlba írja
        #indent=4 → szép formázás
        #ensure_ascii=False → ékezetek megtartása

def dolgozo_hozzaad(dolgozok: list): #Új dolgozó hozzáadása
    nev = input("Add meg a dolgozó nevét: ")
    fizetes = int(input("Add meg a fizetését (Ft): "))
    dolgozok.append(Dolgozo(nev, fizetes)) #Új Dolgozo objektum hozzáadása a listához
    print("Dolgozó hozzáadva!")

def dolgozo_torol(dolgozok: list): #Dolgozó törlése név alapján
    nev = input("Add meg a törlendő dolgozó nevét: ")
    uj_lista = [d for d in dolgozok if d.nev != nev]
    #Új lista létrehozása, amely nem tartalmazza a megadott nevű dolgozót
    if len(uj_lista) == len(dolgozok):  #Ha nem változott a lista hossza
        print("Nincs ilyen nevű dolgozó!")
    else:
        dolgozok[:] = uj_lista  #Az eredeti lista tartalmának cseréje, [:] a lista összes eleme
        print("Dolgozó törölve!")

def dolgozo_modosit(dolgozok: list):
    nev = input("Melyik dolgozó adatait szeretnéd módosítani?: ")
    for d in dolgozok: #Végigmegyünk a dolgozók listáján
        if d.nev == nev: #Ha megtaláljuk a dolgozót
            uj_nev = input("Új név (Enter ha marad): ")
            uj_fiz = input("Új fizetés (Enter ha marad): ")


            if uj_nev:  #Ha nem üres az új név
                d.nev = uj_nev #Név frissítése
            if uj_fiz: #Ha nem üres az új fizetés
                d.fizetes = int(uj_fiz)  #Fizetés frissítése


            print("Adatok frissítve!")
            return  #Kilép a függvényből
    print("Nincs ilyen nevű dolgozó!")

def fizetes_osszeg(dolgozok: list):
    return sum(d.fizetes for d in dolgozok)
     #Visszaadja az összes dolgozó fizetésének összegét



def veletlenszeru_fizetes(dolgozok: list):
    if not dolgozok: #Ha a lista üres
        return None #Nincs eredmény
    return random.choice(dolgozok) #choice véletlenszerűen kiválaszt egy elemet a megadott listából
    #Véletlenszerű dolgozót ad vissza (nem ténylegesen a legmagasabbat)

def legmagasabb_fizetes(dolgozok: list):
    if not dolgozok:                 #Ha üres a lista
        return None                  #Nincs eredmény
    return max(dolgozok, key=lambda d: d.fizetes)
    #A legnagyobb fizetésű dolgozót adja vissza


def legalacsonyabb_fizetes(dolgozok: list):
    if not dolgozok:                 #Ha üres a lista
        return None                  #Nincs eredmény
    return min(dolgozok, key=lambda d: d.fizetes) #key: azt mondja meg mi alapján hasonlítsd össze az elemeket, a min függvénynek
    #d: d.fizetes a d egy ideiglenes változó, egy dolgozót jelent, a dolgozok listából, egyesével
    #A legkisebb fizetésű dolgozót adja vissza


def rendezes_fizetes_szerint(dolgozok: list):
    lista = dolgozok.copy() #Az eredeti lista másolása
    n = len(lista) #Lista hossza
    for i in range(n): #Külső ciklus
        for j in range(n - 1 - i): #Belső ciklus, j = az aktuális index pozíció
            if lista[j].fizetes > lista[j + 1].fizetes:
                #Ha az aktuális elem nagyobb, mint a következő
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Kicseréljük az elemeket
    return lista #Sorba rendezett lista visszaadása

def dolgozo_kereses(dolgozok: list, nev: str):
    for d in dolgozok: #Végigmegyünk a dolgozók listáján
        if d.nev == nev: #Ha egyezik a név
            return d #Visszaadja a megtalált dolgozót
    return None #Ha nincs találat