class Bewoner():
    """Klasse bewonner: bestaat uit een id en naam"""
    def __init__(self, id, naam):
        self.id = id
        self.naam = naam
class Bewoners():
    """Klasse bewonners: bevat bewoner-objecten en verwante bewerkingsmethodes"""

    def __init__(self):
        self.lijst = []
        self.index = 1

    def toevoegen(self,naam):
        nieuwe_bewoner = Bewoner(self.index, naam)
        self.lijst.append(nieuwe_bewoner)
        self.index +=1

    def __str__(self):
        rs = "\n Je vroeg een lijst van bewoners: \n"
        for bewoner in self.lijst:
            rs+= f"\t{str(bewoner.id)}: {bewoner.naam}\n"

        return rs
    