class Kamer():
    """Kamer parameters"""
    def __init__(self, id, kamernaam):
        self.id = id
        self.kamernaam = kamernaam
        self.apparaten = []

    def __str__(self):
        rs = f"{self.id}: {self.kamernaam}\n"
        for apparaat in self.apparaten:
            rs += f"\t\t{apparaat}\n "
        return  rs

class Kamers():
    """Overzicht van alle kamers"""
    def __init__(self):
        self.lijst = []
        self.index =1 

    def toevoegen(self,kamernaam):
        """Tovoegen van kamer in kamerlijst"""
        nieuwe_kamer = Kamer(self.index, kamernaam)
        self.lijst.append(nieuwe_kamer)
        self.index += 1 

    def __str__(self):
        rs = "\nWe hebben enkele kamers:\n"
        for kamer in self.lijst:
            rs+= f"\t{kamer}\n"
        return rs