from abc import ABC, abstractmethod

class Apparaat(ABC): 
    """Apparaat parameters"""
    def __init__(self,id, kamer):
        self.status = False
        self.id = id
        self.kamer = kamer

    def update(self):
        return f"{self.__class__.__name__} in {self.kamer} is aangepast: {self.status}"

    @abstractmethod
    def statusOn(self):
        pass
    @abstractmethod
    def statusOff(self):
        pass
    
    def __str__(self):
        str_status = "On" if self.status else "Off"
        return f"{self.id}: {self.__class__.__name__} {str_status}\n"
    
class Lamp(Apparaat):
    def __init__(self, id, kamer):
        super().__init__(id, kamer)
        self.helderheid = 5
    def update(self):
        return f"{self.__class__.__name__} in {self.kamer} is aangepast: {self.status} {self.helderheid}"

    def statusOn(self):
        self.status = True

    def statusOff(self):
        self.status = False
    
    def helderheid_instellen(self):
        """Helderheid instellen"""
        print("Hoe helder wil je de lamp hebben?")
        helderheid = int(input("1 dim ---- 10 fel: "))
        while helderheid > 10 or helderheid < 1:
            helderheid = int(input("Verkeerde input ingevoerd [1-10]: "))
        self.helderheid = helderheid

    def __str__(self):
        str_status = "On" if self.status else "Off"
        rs = f"{self.id}: {self.__class__.__name__} {str_status}\n"
        rs += f"\t\thelderheid: {self.helderheid}\n"
        return rs
    
class Thermostaat(Apparaat):
    def __init__(self, id, kamer):
        super().__init__(id, kamer)
        self.statusOn()
        self.temp = 20

    def update(self):
        return f"{self.__class__.__name__} in {self.kamer} is aangepast: {self.status} {self.temp}°C"

    def verander_temp(self):
        """Temperatuur instellen"""
        print("Hoe warm wil je het hebben?")
        temp = int(input("5-30°C: "))
        while temp < 5 or temp > 30:
            temp = int(input("Invalid temperature [5-30]: "))
        self.temp = temp
        
    def statusOff(self):
        self.status = False
    
    def statusOn(self):
        self.status = True

    def __str__(self):
        str_status = "On" if self.status else "Off"
        rs = f"{self.id}: {self.__class__.__name__} {str_status}\n"
        rs += f"\t\tThemperature: {self.temp}\n"
        return rs

class Deurslot(Apparaat):
    def __init__(self, id, kamer):
        super().__init__(id, kamer)

    def statusOff(self):
        self.status = False
    
    def statusOn(self):
        self.status = True

    def __str__(self):
        status = "Open" if self.status else "Closed"
        rs = f"{self.id}: {self.__class__.__name__} {status}\n"
        return rs

class Bewegingssensor(Apparaat):
    def __init__(self, id, kamer):
        super().__init__(id, kamer)

    def statusOff(self):
        self.status = False
    
    def statusOn(self):
        self.status = True
    
class Rookmelder(Apparaat):
    def __init__(self, id, kamer):
        super().__init__(id, kamer)

    def alarm(self):
        return f"ALARM GAAT AF IN {self.kamer}"

    def statusOff(self):
        self.status = False
    
    def statusOn(self):
        self.status = True
        self.alarm()
    

class Gordijn(Apparaat):
    def __init__(self,id, kamer):
        super().__init__(id,kamer)

    def statusOff(self):
        self.status = False
    
    def statusOn(self):
        self.status = True

    def __str__(self):
        status = "Open" if self.status else "Closed"
        rs = f"{self.id}: {self.__class__.__name__} {status}\n"
        return rs

class Apparaten():
    """Lijst van apparaten"""
    def __init__(self):
        self.lijst = []
        self.index = 1

    def toevoegen(self, apparaat, kamer):
        """Toevoegen van apparaten in een lijst van apparaten"""
        match apparaat:
            case "Lamp":
                nieuw_apparaat = Lamp(self.index,kamer)
            case "Thermostaat":
                nieuw_apparaat = Thermostaat(self.index, kamer)
            case "Deurslot":
                nieuw_apparaat = Deurslot(self.index, kamer)
            case "Bewegingssensor":
                nieuw_apparaat = Bewegingssensor(self.index,kamer)
            case "Rookmelder":
                nieuw_apparaat = Rookmelder(self.index,kamer)
            case "Gordijn":
                nieuw_apparaat = Gordijn(self.index, kamer)
        
        self.lijst.append(nieuw_apparaat)
        self.index += 1

    def __str__(self):
        rs = "\nLijst van apparaten:\n"
        for apparaat in self.lijst:
            rs += f"\t{apparaat}\n"
        return rs