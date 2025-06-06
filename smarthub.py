class Smarthub():
    def __init__(self,woning, logger):
        self.woning = woning
        self.logger = logger
        self.vorige_kamer = None
        self.vorige_apparaten = None
    
    def finding_devices(self, kamer_movement):
        """Finding the right devices for the right room"""
        for kamer in self.woning.kamers.lijst:
            if kamer.kamernaam == kamer_movement:
                return kamer.apparaten

    def manual_check_up(self,apparaten):
        """Checking devices and interacting with them"""
        
        print(f"\tBewoner staat bij {apparaten[0].kamer}")
        
        if "Thermostaat" == self.looping_through_devices(apparaten, "Thermostaat").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Thermostaat")
            
            antwoord = input("Wil je het temperatuur veranderen [Y/N]: ")
            if antwoord == "Y":
                apparaat.verander_temp()
                self.logger.log(f"TEMP CHANGED TO {apparaat.temp} IN {apparaat.kamer}")

        if "Rookmelder" == self.looping_through_devices(apparaten, "Rookmelder").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Rookmelder")   

        if "Deurslot" == self.looping_through_devices(apparaten, "Deurslot").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Deurslot")   
            if not apparaat.status:
                if self.door_code(apparaat):
                    apparaat.statusOn()
                    self.logger.log(f"DEURSLOT IS {"OPEN" if apparaat.status else "CLOSED"} IN {apparaat.kamer}")
                else:
                    return print("ACCESS DENIED")
                    
                    
        if "Bewegingssensor" == self.looping_through_devices(apparaten, "Bewegingssensor").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Bewegingssensor")   
            if not apparaat.status:
                    apparaat.statusOn()
                    self.logger.log(f"BEWEGINGSSENSOR IS {apparaat.status} IN {apparaat.kamer}")

        if "Lamp" == self.looping_through_devices(apparaten, "Lamp").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Lamp")           
            bew_apparaat = self.looping_through_devices(apparaten, "Bewegingssensor")   
            if bew_apparaat:
                apparaat.statusOn()
                self.logger.log(f"{apparaat.id}: LAMP IS {"ON" if apparaat.status else "OFF"} IN {apparaat.kamer}")

            antwoord = input("Wil je de helderheid aanpassen [Y/N]: ")
            if antwoord == "Y":
                apparaat.helderheid_instellen()
                self.logger.log(f"LAMP SETTING CHANGED {apparaat.helderheid} IN {apparaat.kamer}")

        if "Gordijn" == self.looping_through_devices(apparaten, "Gordijn").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Gordijn")   
            if apparaat.status:
                antwoord = input("Wil je de gordijnen sluiten [Y/N]: ")
                if antwoord == "Y":
                    apparaat.statusOff()
                    self.logger.log(f"GORDIJN IS {apparaat.status} IN {apparaat.kamer}")

            else:
                antwoord = input("Wil je de gordijnen open [Y/N]: ")
                if antwoord == "Y":
                    apparaat.statusOn()
                    self.logger.log(f"GORDIJN IS {apparaat.status} IN {apparaat.kamer}")

    def looping_through_devices(self, apparaten, apparaat_naam):
        for apparaat in apparaten:
            if apparaat.__class__.__name__ == apparaat_naam:
                return apparaat

    def door_code(self,apparaat):
        password = 1234
        print("DOOR IS CLOSED")
        input_password = int(input("PASSWWORD PLEASE [CODE=1234]: "))
        while True:
            if input_password == password:
                print("PASSWORD CORRECT: ACCESS AUTHORIZED")
                self.logger.log(f"INPUT: {input_password}, PASSWORD CORRECT: ACCESS AUTHORIZED IN {apparaat.kamer}")
                return True
            else:
                print("PASSWORD INCORRECT: ACCES DENIED")
                self.logger.log(f"INPUT: {input_password}, PASSWORD INCORRECT: ACCESS DENIED IN {apparaat.kamer}")
                rematch = input("Try again or Quit or Bruteforce [T/Q/B]: ")
                if rematch == "Q":
                    return False
                if rematch == "B":
                    self.bruteforce(str(password))
                    return True
                input_password = int(input("PASSWWORD PLEASE: "))


    def simulatie(self, apparaten):
        """Simulatie opstarten"""
        if self.vorige_kamer == apparaten[0].kamer or self.vorige_kamer == None:
            print(f"\tBewoner blijft in {self.vorige_kamer}")
            pass
        else:
            Bapp = self.looping_through_devices(self.vorige_apparaten,"Bewegingssensor")
            Lapp = self.looping_through_devices(self.vorige_apparaten,"Lamp")
            Dapp = self.looping_through_devices(self.vorige_apparaten,"Deurslot")
            Bapp.statusOff()
            Lapp.statusOff()
            Dapp.statusOff()
            self.logger.log(f"BEWEGINGSSENSOR IS {Bapp.status} IN {Bapp.kamer}")
            self.logger.log(f"LAMP IS {"ON" if Lapp.status else "OFF"} IN {Lapp.kamer}")
            self.logger.log(f"DEURSLOT IS {"OPEN" if Dapp.status else "CLOSED"} IN {Dapp.kamer}")
            print(f"\tBewoner wandelt uit kamer")
            print(f"\tBEWEGINGSSENSOR IS {Bapp.status} IN {Bapp.kamer}")
            print(f"\tLAMP IS {"ON" if Lapp.status else "OFF"} IN {Lapp.kamer}")
            print(f"\tDEURSLOT IS {"OPEN" if Dapp.status else "CLOSED"} IN {Dapp.kamer}")
            print("--------------------------------------------------------------")
            
        if "Rookmelder" == self.looping_through_devices(apparaten, "Rookmelder").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Rookmelder") 
            if(False):
                apparaat.statusOn()
                self.logger.log(apparaat.alarm())

        if "Deurslot" == self.looping_through_devices(apparaten, "Deurslot").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Deurslot")   
            if not apparaat.status:
                print(f"\tBewoner voert DEURSLOT CODE IN 1234 IN {apparaat.kamer}")
                apparaat.statusOn()  
                print(f"\tDEURSLOT IS {"OPEN" if apparaat.status else "CLOSED"} IN {apparaat.kamer}")
                self.logger.log(f"DEURSLOT IS {"OPEN" if apparaat.status else "CLOSED"} IN {apparaat.kamer}")
                print(f"\tBewoner wandert {apparaat.kamer} binnen")

        if "Bewegingssensor" == self.looping_through_devices(apparaten, "Bewegingssensor").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Bewegingssensor")   
            if not apparaat.status:
                apparaat.statusOn()
                print(f"\tBEWEGINGSSENSOR IS {apparaat.status} IN {apparaat.kamer}")

            self.logger.log(f"BEWEGINGSSENSOR IS {apparaat.status} IN {apparaat.kamer}")

        if "Lamp" == self.looping_through_devices(apparaten, "Lamp").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Lamp")   
            bew_apparaat = self.looping_through_devices(apparaten, "Bewegingssensor")   
            if bew_apparaat:
                apparaat.statusOn()
            else: 
                apparaat.statusOff()
            print(f"\tLAMP IS {"ON" if apparaat.status else "OFF"} IN {apparaat.kamer}")
            self.logger.log(f"LAMP IS {"ON" if apparaat.status else "OFF"} IN {apparaat.kamer}")

        if "Gordijn" == self.looping_through_devices(apparaten, "Gordijn").__class__.__name__:
            apparaat = self.looping_through_devices(apparaten, "Gordijn")   
            print(f"\tGORDIJN IS {"OPEN" if apparaat.status else "CLOSED"} IN {apparaat.kamer}")
            self.logger.log(f"GORDIJN IS {apparaat.status} IN {apparaat.kamer}")
        self.vorige_kamer = apparaten[0].kamer
        self.vorige_apparaten = apparaten
    

    def bruteforce(self, password):
        
        print("Entering BruteForce")
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        bruteforce_wachtwoord = f"{i}{j}{k}{l}"
                        if bruteforce_wachtwoord == password:
                            self.logger.log(f"Bruteforce unlocked: {bruteforce_wachtwoord}")
                            return print(f"Unlocked: {bruteforce_wachtwoord}")
                        
        return print("BRUTEFORCE FAILED")