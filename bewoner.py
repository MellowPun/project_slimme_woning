class Bewoner():
    """bewonner parameters"""
    def __init__(self, id, naam):
        self.id = id
        self.naam = naam
        self.locatie = "gang"
    def __str__(self):
        rs = f"{self.id}: {self.naam}\n"
        rs += f"\tLocated: {self.locatie}\n"
        return rs
class Bewoners():
    """Bewoners lijst"""

    def __init__(self):
        self.lijst = []
        self.index = 1

    def toevoegen(self,naam):
        nieuwe_bewoner = Bewoner(self.index, naam)
        self.lijst.append(nieuwe_bewoner)
        self.index +=1

    def __str__(self):
        rs = "\nLijst van bewoners: \n"
        for bewoner in self.lijst:
            rs += f"\t{bewoner}\n"
        return rs