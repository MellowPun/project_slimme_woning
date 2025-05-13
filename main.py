from woning import Woning
from smarthub import Smarthub
from logger import Logger
from random import randint

woning = Woning()
logger = Logger()
smarthub = Smarthub(woning, logger)
kamers =  ["woonkamer","keuken","slaapkamer_1","slaapkamer_2","badkamer","gang"]

steps = int(input("Hoeveel stappen wil je hebben:"))
for _ in range(steps):
    randnum = randint(0,5)
    woning.bewoners.locatie_aanpassen(1,kamers[randnum])
    lijst_apparaten = smarthub.finding_devices(kamers[randnum])

    smarthub.manual_check_up(lijst_apparaten)

logger.toon_logger()


#while True:

    #print("[1] Start a simulation")
    #print("[2] Toon de Logger")
    #print("[3] Verander manueel de settings")
    #option = int(input("Welke optie wil je [1-3]:"))
    #match option:
        #case 1:
            #steps = int(input("Hoeveel stappen wil je hebben:"))
            #for _ in range(steps):
                #randnum = randint(0,5)
                #woning.bewoners.locatie_aanpassen(1,kamers[randnum])
                #lijst_apparaten = smarthub.finding_devices(kamers[randnum])

                #smarthub.manual_check_up(lijst_apparaten)
