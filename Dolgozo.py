class Dolgozo:
    def __init__(self, nev: str, fizetes: int):
        self.nev = nev
        self.fizetes = fizetes


    def to_dict(self):
        return {"nev": self.nev, "fizetes": self.fizetes}