from woning import Woning
from logger import Logger
from smarthub import Smarthub
from random import randint
from HTMLGen import html

woning = Woning()
logger = Logger()
smarthub = Smarthub(woning, logger)
html_gen = html(woning)
kamers =  ["woonkamer","keuken","slaapkamer_1","slaapkamer_2","badkamer","gang"]
for apparaat in woning.kamers.lijst[5].apparaten:
    print(apparaat)


while True:
    
    print("[1] Start a simulation")
    print("[2] Toon de Logger")
    print("[3] Verander manueel de settings")
    print("[4] Bruteforce")
    print("[5] Stop")
    option = int(input("Welke optie wil je [1-5]:"))
    match option:

        case 1:
            steps = int(input("Hoeveel stappen wil je hebben:"))
            for i in range(steps):
                print()
                print(f"============================STAP {i+1}============================")
                print()
                randnum = randint(0,5)
                woning.bewoners.locatie_aanpassen(1,kamers[randnum])
                logger.log(f"{woning.bewoners.lijst[0].naam} MOVES TO {kamers[randnum]}")
                lijst_apparaten = smarthub.finding_devices(kamers[randnum])
                smarthub.simulatie(lijst_apparaten)
                print()
                logger.write_Json()
            html_gen.genereer_html()    

        case 2: 
            logger.toon_logger()

        case 3:
            steps = int(input("Hoeveel stappen wil je hebben:"))
            for i in range(steps):
                print()
                print(f"============================STAP {i+1}============================")
                print()
                randnum = randint(0,5)
                woning.bewoners.locatie_aanpassen(1,kamers[randnum])
                lijst_apparaten = smarthub.finding_devices(kamers[randnum])
                smarthub.manual_check_up(lijst_apparaten)
                print()

        case 4:
            smarthub.bruteforce("1234")
        case 5:
            print("Goodbye")
            break


