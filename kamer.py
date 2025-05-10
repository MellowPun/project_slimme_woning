class Kamer():
    """Klasse kamer: bestaat uit een id en kamernaam"""
    def __init__(self,id, kamer):
        self.id = id
        self.kamer = kamer
        
class Kamers():
    """Klasse kamers: bevat kamers-objecten en verwante bewerkingsmethodes"""
    def __init__(self):
        self.lijst = []
        self.index = 1

    def toevoegen(self,kamer):
        nieuwe_kamer = Kamer(self.index, kamer)
        self.lijst.append(nieuwe_kamer)
        self.index +=1
    
    def __str__(self):
        rs = "\n We hebben enkele kamers:\n"
        for kamer in self.lijst:
            rs+= f"\t{str(kamer.id)}: {kamer.naam}\n"

        return rs