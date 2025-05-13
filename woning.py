from kamer import Kamers
from apparaat import Apparaten
from bewoner import Bewoners


class Woning():
    def __init__(self):
        self.kamers = Kamers()
        self.apparaten = Apparaten()
        self.bewoners = Bewoners()
        self.initialiseer_kamers()
        self.initialiseer_apparaten()
        self.initialiseer_bewoners()
        self.apparaat_kamers_link()
        

    def initialiseer_kamers(self):
       for kamer in [
            "woonkamer",
            "keuken",
            "slaapkamer_1",
            "slaapkamer_2",
            "badkamer",
            "gang"
       ]:
           self.kamers.toevoegen(kamer)

    def initialiseer_apparaten(self):
        for apparaat in [
            ["Lamp", "woonkamer"],
            ["Lamp", "keuken"],
            ["Lamp", "slaapkamer_1"],
            ["Lamp", "slaapkamer_2"],
            ["Lamp", "badkamer"],
            ["Lamp", "gang"],
            ["Thermostaat", "gang"],
            ["Deurslot", "woonkamer"],
            ["Deurslot", "keuken"],
            ["Deurslot", "slaapkamer_1"],
            ["Deurslot", "slaapkamer_2"],
            ["Deurslot", "badkamer"],
            ["Deurslot", "gang"],
            ["Bewegingssensor", "woonkamer"],
            ["Bewegingssensor", "keuken"],
            ["Bewegingssensor", "slaapkamer_1"],
            ["Bewegingssensor", "slaapkamer_2"],
            ["Bewegingssensor", "badkamer"],
            ["Bewegingssensor", "gang"],
            ["Rookmelder", "woonkamer"],
            ["Rookmelder", "keuken"],
            ["Rookmelder", "gang"],
            ["Gordijn", "woonkamer"],
            ["Gordijn", "keuken"],
            ["Gordijn", "slaapkamer_1"],
            ["Gordijn", "slaapkamer_2"],
        ]:
            self.apparaten.toevoegen(apparaat[0],apparaat[1])
            
    def initialiseer_bewoners(self):
        for bewoner in [
            "Axel",
            "Benji",
            "Carlos",
            "Beatrix"
        ]:
            self.bewoners.toevoegen(bewoner)
    
    def apparaat_kamers_link(self):
        """Loopen door kamerlijst en apparatenlijst. 
        Bekijken welke apparaten in een bepaalde kamer zit 
        en deze toeveogen aan de lijst van kamers."""
        for kamer in self.kamers.lijst:
            for apparaat in self.apparaten.lijst:
                if kamer.kamernaam == apparaat.kamer:
                    kamer.apparaten.append(apparaat)
                    
