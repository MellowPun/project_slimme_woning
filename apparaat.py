from abc import ABC, abstractmethod
class Apparaat(ABC):
    """Klasse Apparaten: bevat apparaten-objecten en verwante bewerkingsmethodes"""
    def __init__(self):
        super().__init__()
        status = False

    @abstractmethod
    def statusOn(self):
        pass

    def statusOff(self):
        pass

class Lamp(Apparaat):
    instances = []
    def __init__(self,id, kamer):
        self.apparaatIndex= id
        self.kamer = kamer
        self.__helderheid = 3
        self.id = 1
        Lamp.instances.append(self)

    def statusOff(self):
        self.status = False
    
    def statusOn(self):
        self.status = True
    
    def helderheid(self, id):
        print("Hoe helder wil je de lamp hebben?")
        helderheid = int(input("1 dim ---- 5 fel: "))
        while helderheid > 5 or helderheid < 0:
            helderheid = int(input("Verkeerde input ingevoerd [1-5]: "))
        self.__helderheid = helderheid


class Thermostaat(Apparaat):
    instances = []
    def __init__(self, id, kamer):
        self.kamer  = kamer
        self.apparaatIndex = id
        self.temp = 20
        Thermostaat.instances.append(self)
    def verander_temp(self, id):
        print("Hoe warm wil je het hebben?")
        temp = int(input("5-30°C: "))
        while temp < 5 or temp > 30:
            temp = int(input("Invalid temperature [5-30]: "))
        self.temp = temp


class Deurslot(Apparaat):
    



class Apparaten():
    """Klasse Apparaten: bevat apparaten-objecten en verwante bewerkingsmethodes"""

    def __init__(self):
        self.lijst = []
        self.index = 1
    
    def toevoegen(self, apparaat, kamer):
        match apparaat:
            case "Lamp":
                nieuw_apparaat = Lamp(self.index,kamer)
            case "Thermostaat":
                nieuw_apparaat = Thermostaat(self.index, kamer)
            case "Deurslot":
                nieuw_apparaat = Deurslot(self.index, kamer)
            case "Bewegingssensor":
                nieuw_apparaat = Bewegingssensor(self.index, kamer)
            case "Rookmelder":
                nieuw_apparaat = Rookmelder(self.index, kamer)
            case "Gordijn":
                nieuw_apparaat = Gordijn(self.index, kamer)
            case _:
                print("Unknown Object")

    