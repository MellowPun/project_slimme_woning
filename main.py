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
def bruteforce():
    wachtwoord = "0000"
    print("Entering BruteForce")
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    bruteforce_wachtwoord = f"{i}{j}{k}{l}"
                    if bruteforce_wachtwoord == wachtwoord:
                        return print(f"Unlocked: {bruteforce_wachtwoord}")
                    
    return print("BRUTEFORCE FAILED")


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
            for _ in range(steps):
                randnum = randint(0,5)
                woning.bewoners.locatie_aanpassen(1,kamers[randnum])
                logger.log(f"{woning.bewoners.lijst[0].naam} MOVES TO {kamers[randnum]}")
                lijst_apparaten = smarthub.finding_devices(kamers[randnum])
                smarthub.simulatie(lijst_apparaten)
                logger.write_Json()
            html_gen.genereer_html()    

        case 2: 
            logger.toon_logger()

        case 3:
            steps = int(input("Hoeveel stappen wil je hebben:"))
            for _ in range(steps):
                randnum = randint(0,5)
                woning.bewoners.locatie_aanpassen(1,kamers[randnum])
                lijst_apparaten = smarthub.finding_devices(kamers[randnum])
                smarthub.manual_check_up(lijst_apparaten)
        
        case 4:
            bruteforce()
        case 5:
            print("Goodbye")
            break


