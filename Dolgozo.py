class Dolgozo:
    def __init__(self, nev: str, fizetes: int): #konstruktor inicializáló függvény
        self.nev = nev #A self mindig az aktuális objektumra hivatkozik
        self.fizetes = fizetes


    def to_dict(self): #Ez egy függvény az osztályban, ami az objektum adatainak lekérésére szolgál 
        #Név: to_dict = a cél, hogy szótárba (dictionary) alakítsa az objektumot. 
        # A self itt is az aktuális objektumra utal
        return {"nev": self.nev, "fizetes": self.fizetes}