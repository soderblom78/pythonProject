import time
import emoji

def main():

    # Bilhallen

    # importerade moduler
    import bilfirman_anställda
    import bilfirman_försäljning
    import bilfirman_verkstad
    import keyboard
    from os import system, name

    # Funktion för att rensa skärmen
    def clear():
        if name == "nt":
            _ = system("cls")

    # Funktioner, meny 1-3 + undermeny 1-3
    def meny_admin():
        print("---> Admin")
        print("Försäljning")
        print("Verkstad")
        print("Avsluta")

    def undermeny_personal():
        print("Admin")
        print("---> Personal")
        print("     Kunder, försäljning")
        print("     Kunder, verkstad")
        print("Försäljning")
        print("Verkstad")
        print("Avsluta")

    def undermeny_kunder_försäljning():
        print("Admin")
        print("     Personal")
        print("---> Kunder, försäljning")
        print("     Kunder, verkstad")
        print("Försäljning")
        print("Verkstad")
        print("Avsluta")

    def undermeny_kunder_verkstad():
        print("Admin")
        print("     Personal")
        print("     Kunder, försäljning")
        print("---> Kunder, verkstad")
        print("Försäljning")
        print("Verkstad")
        print("Avsluta")

    def meny_försäljning():
        print("Admin")
        print("---> Försäljning")
        print("Verkstad")
        print("Avsluta")

    def meny_verkstad():
        print("Admin")
        print("Försäljning")
        print("---> Verkstad")
        print("Avsluta")

    def meny_avsluta():
        print("Admin")
        print("Försäljning")
        print("Verkstad")
        print("---> Avsluta")

    meny_vald = 1
    undermeny_vald = 1

    while True:
        clear()
        # Printar ut vilken meny användaren är inne i. Här är det Huvudmenyn
        print("\nBILFIRMAN: HUVUDMENY\n")
        print("\nGör ett val med piltangenterna upp eller ned. tryck HÖGER PIL för att välja!\n")

        # Från modulen keyboard, registrerar vilken tangent på tangentbordet användaren har tryckt in.
        # Med vilkorens hjälp testas vilken tangent användaren har tryckt ned, samt vilken meny eller
        # undermeny som är vald.
        # I det här fallet testas: Pil ned, Pil upp, Pil höger, Pil vänster
        if keyboard.is_pressed("down arrow") and meny_vald < 4 and undermeny_vald == 1:
            meny_vald += 1
        elif keyboard.is_pressed("up arrow") and meny_vald > 1 and undermeny_vald == 1:
            meny_vald -= 1
        elif keyboard.is_pressed("right arrow") and meny_vald == 1:
            undermeny_vald += 1
        elif keyboard.is_pressed("down arrow") and meny_vald == 1 and undermeny_vald < 4:
            undermeny_vald += 1
        elif keyboard.is_pressed("down arrow") and meny_vald == 1 and undermeny_vald == 4:
            undermeny_vald = 1
        elif keyboard.is_pressed("up arrow") and meny_vald == 1 and undermeny_vald > 1:
            undermeny_vald -= 1
        elif keyboard.is_pressed("left arrow") and meny_vald == 1 and undermeny_vald > 1:
            undermeny_vald = 1

        elif meny_vald == 1 and undermeny_vald == 1:
            meny_admin()
        elif meny_vald == 1 and undermeny_vald == 2:
            undermeny_personal()
        elif meny_vald == 1 and undermeny_vald == 3:
            undermeny_kunder_försäljning()
        elif meny_vald == 1 and undermeny_vald == 4:
            undermeny_kunder_verkstad()
        elif meny_vald == 2:
            meny_försäljning()
        elif meny_vald == 3:
            meny_verkstad()
        elif meny_vald == 4:
            meny_avsluta()

        # Från modulen keyboard, stoppar och läser av användarens tryckta tangent
        keyboard.read_key()

        # Vilkoret testar om användaren tryckt in Höger pil och att undermeny vald = 1 (det vill säga det
        # ursprungliga värdet som betyder att användaren inte är inne i någon undermeny)
        if keyboard.is_pressed("right arrow") and undermeny_vald == 1:

            if meny_vald == 2:
                clear()
                meny_vald = 1

                # En annan fil, annat script öppnas, Bilfirman försäljning
                bilfirman_försäljning.main()
                main()

            # En annan fil, annat script öppnas, Bilfirman verkstad
            if meny_vald == 3:
                clear()
                meny_vald = 1
                bilfirman_verkstad.main()
                main()

            # Programmet avslutas
            if meny_vald == 4:
                clear()
                print("\nTack så mycket för att du kämpat dig igenom programmet!\nHA EN FANTASTISK DAG!!")
                print("\U0001F606")
                time.sleep(2)
                quit()

        # Vilkoret testar om användaren tryckt in Höger pil och att undermeny vald = 2 (det vill säga att
        # användaren är i en undermeny)
        if keyboard.is_pressed("right arrow") and undermeny_vald == 2:
            clear()
            undermeny_vald = 1
            # En annan fil, annat script öppnas, Bilfirman Anställda
            # Här kan den administrativa anställda ta del av en lista på uppgifter om dom anställda
            bilfirman_anställda.main()
            main()

        # Vilkoret testar om användaren tryckt in Höger pil och att undermeny vald = 3
        if keyboard.is_pressed("right arrow") and undermeny_vald == 3:
            clear()
            print("\nBILFIRMAN: KUNDER, FÖRSÄLJNING")

            # En textfil öppnas, Bilfirman försäljning.txt
            # Här kan den administrativa anställda ta del av kunduppgifter och försäljningsprospekt
            open("bilfirman_försäljning.txt", "r")
            with open("bilfirman_försäljning.txt") as f:
                contents = f.read()
                print(contents)
                input("\nTryck enter för att komma till huvudmeny!")
                undermeny_vald = 1
                continue

        # En textfil öppnas, Bilfirman verkstad.txt
        # Här kan den administrativa anställda ta del av kund och biluppgifter samt verkstadsbokningar
        if keyboard.is_pressed("right arrow") and undermeny_vald == 4:
            clear()
            print("\nBILFIRMAN: KUNDER, VERKSTAD")
            open("bilfirman_verkstad.txt", "r")
            with open("bilfirman_verkstad.txt") as f:
                contents = f.read()
                print(contents)
                input("\nTryck enter för att komma till huvudmeny!")
                undermeny_vald = 1
                continue


if __name__ == "__main__":
    main()
















































