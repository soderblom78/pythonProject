# bilfirman_verkstad

def main():
    import slutuppdrag
    from os import system, name
    import keyboard
    import datetime
    from datetime import date

    # Funktion för att rensa skärmen
    def clear():
        if name == "nt":
            _ = system("cls")

    # Funktion för dagens datum och tid
    tid = datetime.datetime.now()

    # Sparar tid i string variabel
    tiden = ""
    tiden = str(tid)

    # Sparade listor
    sparat_reg_nummer = []
    sparat_bilmärke = []
    sparat_modell = []
    sparat_årsmodell = []
    sparat_antal_kilometer = []

    lagrat_personnummer = []
    lagrat_namn = []
    lagrat_mail = []
    lagrat_telefon = []

    skada = []
    sparad_skada = []
    sparade_biluppgifter = []
    sparade_personppgifter = []
    lagrade_personuppgifter = []
    lagrade_biluppgifter = []

    # Funktionen kallas när användaren ska mata in sina biluppgifter.
    # Testar om användaren vid ett tidigare tillfälle redan matat in ett registreringsnummer
    # Funktionen hjälper isåfall till att skriva ut sparade uppgifter som hör till inmatat registreringsnummer.

    def bil_uppgifter():
        if reg_nummer in sparat_reg_nummer:
            indexnummer = (sparat_reg_nummer.index(reg_nummer))
            print("\nDen bilen finns redan sparad i vårt register:")
            print("Bilmärke: " + sparat_bilmärke[indexnummer])
            print("Bilmodell: " + sparat_modell[indexnummer])
            print("Årsmodell: " + sparat_årsmodell[indexnummer])
            print("Antal kilometer: " + sparat_antal_kilometer[indexnummer])

        else:
            sparat_reg_nummer.append(reg_nummer)
            bilmärke = input("Vilket bilmärke har du?: ")
            sparat_bilmärke.append(bilmärke)
            modell = input("Vilken modellbeteckning?: ")
            sparat_modell.append(modell)
            årsmodell  = input("Vilken årsmodell?: ")
            sparat_årsmodell.append(årsmodell)
            while True:
                antal_kilometer = input("Hur långt har den gått?, antal kilometer: ")
                try:
                    antal_kilometer = int(antal_kilometer)
                except ValueError:
                    print("Kan du skriva det i siffror tack!")
                else:
                    break
            antal_kilometer = str(antal_kilometer)
            sparat_antal_kilometer.append(antal_kilometer)

    # Funktionen kallas när användaren ska mata in sina personuppgifter.
    # Testar om användaren vid ett tidigare tillfälle redan matat in ett personnummer.
    # Funktionen hjälper isåfall till att skriva ut sparade uppgifter som hör till inmatat personnummer.

    def personuppgifter():
        if personnummer in lagrat_personnummer:
            indexnummer = (lagrat_personnummer.index(personnummer))
            print("\nDu finns redan sparad i vårt register:")
            print("Namn: " + lagrat_namn[indexnummer])
            print("Mail: " + lagrat_mail[indexnummer])
            print("Telefon: " + lagrat_telefon[indexnummer])

        else:
            lagrat_personnummer.append(personnummer)
            namn = input("Förnamn och Efternamn?: ")
            lagrat_namn.append(namn)
            mail = input("Mailadress: ")
            lagrat_mail.append(mail)
            telefon  = input("Telefonnummer: ")
            lagrat_telefon.append(telefon)

        input("\nTack så mycket! Tryck enter för att komma vidare:")

    # Funktion som kallas när man gör en skadeanmälan under verkstadsdelen - reperation och garantiärenden
    # Användaren skriver vad som är fel på bilen, högsta antal rader för textinmatning = 5
    # Om användaren trycker enter utan att ha skrivit något på raden bryts och sparas textinmatningen

    def skadeanmälan():
        skada.clear()
        x = range(5)
        for i in x:
            i = input()
            if len(i) == 0:
                break
            else:
                skada.append(i)

    # Funktioner för menyval

    def meny_service():
        print("\n---> Service")
        print("Reparation")
        print("Tillbaks till huvudmeny")

    def meny_reparation():
        print("\nService")
        print("---> Reparation")
        print("Tillbaks till huvudmeny")

    def meny_huvudmeny():
        print("\nService")
        print("Reparation")
        print("---> Tillbaka till huvudmeny")

    meny_vald = 1   # Håller reda på vilken meny som är vald (pil ned = meny_vald +1 pil upp = meny_vald -1)

    # While loop, kör programmet tills det anropas att det ska brytas
    # eller lämnas genom att välja menyval huvudmeny
    while True:
        clear()
        print("\nBILFIRMAN: VERKSTAD\n")
        print("\nGör ett val med piltangenterna upp eller ned. tryck HÖGER PIL för att välja!\n")

        # Från modulen keyboard, känner av om användaren trycker ned pil ner eller pil upp
        # Med vilkorens hjälp testar jag vilken tangent användaren har tryckt ned och vilka vilkor som gäller
        if keyboard.is_pressed("down arrow") and meny_vald < 3:
            meny_vald += 1
        elif keyboard.is_pressed("up arrow") and meny_vald > 1:
            meny_vald -= 1

        elif meny_vald == 1:
            meny_service()
        elif meny_vald == 2:
            meny_reparation()
        elif meny_vald == 3:
            meny_huvudmeny()

        # Från modulen keyboard, stoppar och läser av användarens tryckta tangent
        keyboard.read_key()

        # Menyval Service, väljs genom att trycka enter
        if keyboard.is_pressed("right arrow") and meny_vald == 1:

            # Rensar skärmen.
            clear()

            # Hälsar kunden välkommen.
            print("\nHej och välkommen till Bilfirmans verkstad!")
            print("\nVi utför service på följande bilmärken: KIA, Volvo och Ford")
            print("För alla verkstadsärenden behöver vi uppgifter om din bil samt lite personuppgifter")

            # Jag har satt inmatning av registreringsnummer utanför funktionen för att jag behöver
            # inmatad uppgift till ett indexnummer som ska hålla koll på rätt bilar till rätt reg.nummer
            reg_nummer = input("\nBilens registreringsnummer: ")

            # Kallar på funktionen för inmatning av resterande biluppgifter
            bil_uppgifter()

            # Det samma gäller inmatning av personnummer
            personnummer = input("\nSkriv ditt personnummer, (10 siffror): ")
            personuppgifter()

            clear()
            indexnummer_bil = (sparat_reg_nummer.index(reg_nummer))
            indexnummer_person = (lagrat_personnummer.index(personnummer))

            # En uträkning för att få fram bilens antal mil som jag behöver i min text senare
            kilometer = sparat_antal_kilometer[indexnummer_bil]
            mil = int(kilometer) / 10
            mil = int(mil)

            # Kör en while loop med olika vilkor, testar om användaren har en bilmodell som
            # bilfirman kan serva. Om inte, skickas användaren tillbaka till menyn.
            while True:
                print("\nBilfirmans verkstad utför service på följande bilmärken: KIA, Volvo och Ford")

                if sparat_bilmärke[indexnummer_bil] == "volvo":
                    print("Vi hjälper dig gärna med service på din Volvo")
                elif sparat_bilmärke[indexnummer_bil] == "kia":
                    print("Vi hjälper dig gärna med service på din Kia")
                elif sparat_bilmärke[indexnummer_bil] == "ford":
                    print("Vi hjälper dig gärna med service på din Ford")
                else:
                    input("Tyvärr kan vi inte hjälpa till och serva din " + sparat_bilmärke[indexnummer_bil] + " Tryck enter för att komma till Menyn")
                    break

                # Användaren får en bekräftelse på att bilen bokas in på service
                print("\nDå bokar vi in en " + str(mil) + " mila service på din " + sparat_bilmärke[indexnummer_bil])
                input("Tack så mycket! Tryck enter för att komma till menyn:")

                # Innan jag skriver över sparade personuppgifter till en gemensam lista, raderar jag
                # eventuell tidigare data
                sparade_personppgifter.clear()
                lagrade_personuppgifter.clear()
                for i in lagrat_namn[indexnummer_person], lagrat_personnummer[indexnummer_person], lagrat_mail[indexnummer_person], lagrat_telefon[indexnummer_person]:
                    sparade_personppgifter.append(i)

                lagrade_personuppgifter.append("\n".join(map(str, sparade_personppgifter)))

                # Innan jag skriver över sparade biluppgifter till en gemensam lista, raderar jag
                # eventuell tidigare data
                sparade_biluppgifter.clear()
                lagrade_biluppgifter.clear()
                for i in sparat_reg_nummer[indexnummer_bil], sparat_bilmärke[indexnummer_bil], sparat_modell[indexnummer_bil], sparat_årsmodell[indexnummer_bil]:
                    sparade_biluppgifter.append(i)

                lagrade_biluppgifter.append("\n".join(map(str, sparade_biluppgifter)))

                # Samlad information om personuppgifter och biluppgifter skickas till en txt.fil
                with open("bilfirman_verkstad.txt", "a") as f:
                    f.write("\n")
                    f.write(tiden)
                    f.writelines("\n\n")
                    f.writelines(lagrade_personuppgifter[-1])
                    f.writelines("\n""\n")
                    f.write("Service:")
                    f.writelines("\n")
                    f.writelines(lagrade_biluppgifter[-1])
                    f.write("\n")

                # loopen bryts och användaren skickas tillbaka till menyn.
                break

        # Menyval Reperation, väljs genom att trycka enter
        elif keyboard.is_pressed("right arrow") and meny_vald == 2:
            clear()
            print("\nHej och välkommen till Bilfirmans verkstad!")
            print("\nVi utför reparationer på följande bilmärken: KIA, Volvo och Ford.")
            print("Är din bil nyare än 6 år så gäller fortfarande nybilsgarantin och skadan kan vara ett garantiärende.")
            print("För alla verkstadsärenden behöver vi uppgifter om din bil samt lite personuppgifter")

            reg_nummer = input("\nBilens registreringsnummer: ")
            bil_uppgifter()

            personnummer = input("\nSkriv ditt personnummer, (10 siffror): ")
            personuppgifter()

            clear()
            indexnummer_bil = (sparat_reg_nummer.index(reg_nummer))
            indexnummer_person = (lagrat_personnummer.index(personnummer))

            if sparat_bilmärke[indexnummer_bil] == "volvo" or sparat_bilmärke[indexnummer_bil] == "kia" or \
                    sparat_bilmärke[indexnummer_bil] == "ford":
                # Användaren har ett bilmärke som bilfirman kan ta in för reperation (Kia, Volvo eller Ford)
                # Användaren ombeds beskriva skadan på max 5 rader.
                print("Beskriv skadan på bilen, max 5 rader")
                skadeanmälan()
                clear()
                print("Vi har tagit emot din skadeanmälan på följande bil:")
                print("En " + sparat_bilmärke[indexnummer_bil] + " " + sparat_modell[indexnummer_bil]
                      + " med registreringsnummer: " + sparat_reg_nummer[indexnummer_bil])
                print("\nI din skadeanmälan har du skrivit:")
                sparad_skada.clear()
                sparad_skada.append("\n".join(map(str, skada)))
                print("\n".join(map(str, skada)))

                # En uträkning för att bestämma om bilen har nybilsgaranti, räknar ut aktuellt år - bilens år.
                today = date.today()
                år = today.strftime("%Y")
                idag_år = int(år)
                bilens_år = int(sparat_årsmodell[indexnummer_bil])
                uträknat_år = idag_år-bilens_år

                # Om bilen är nyare än 6 år så gäller garantin
                # Testar med vilkor.
                if uträknat_år < 6:
                    print("\nEftersom din bil är yngre än 6 år så gäller fortfarande nybilsgarantin och skadan kan vara ett garantiärende")
                else:
                    print("\nEftersom din bil är äldre än 5 år så gäller inte nybilsgarantin och skadan kommer inte behandlas som ett garantiärende")
                input("\nTack så mycket! Vi kommer höra av oss till dig om en tid som passar\n"
                      "Tryck Enter för att komma till menyn")

                meny_vald = 1

                sparade_personppgifter.clear()
                lagrade_personuppgifter.clear()

                for i in lagrat_namn[indexnummer_person], lagrat_personnummer[indexnummer_person], lagrat_mail[indexnummer_person], lagrat_telefon[indexnummer_person]:
                    sparade_personppgifter.append(i)
                lagrade_personuppgifter.append("\n".join(map(str, sparade_personppgifter)))

                sparade_biluppgifter.clear()
                lagrade_biluppgifter.clear()

                for i in sparat_reg_nummer[indexnummer_bil], sparat_bilmärke[indexnummer_bil], sparat_modell[indexnummer_bil], sparat_årsmodell[indexnummer_bil]:
                    sparade_biluppgifter.append(i)
                lagrade_biluppgifter.append("\n".join(map(str, sparade_biluppgifter)))

                with open("bilfirman_verkstad.txt", "a") as f:
                    f.write("\n")
                    f.write(tiden)
                    f.writelines("\n\n")
                    f.writelines(lagrade_personuppgifter[-1])
                    f.writelines("\n""\n")
                    if uträknat_år < 6:
                        f.write("Reperation, nybilsgaranti:")
                    else:
                        f.write("Reperation:")
                    f.writelines("\n")
                    f.writelines(lagrade_biluppgifter[-1])
                    f.writelines("\n""\n")
                    f.write("Beskrivning av skada:")
                    f.write("\n")
                    f.writelines(sparad_skada[-1])
                    f.write("\n")

            else:
                print("Vi utför ej reparationer på " + sparat_bilmärke[indexnummer_bil] + " tyvärr!")
                input("Tryck Enter för att komma till menyn")
                meny_vald = 1

        elif keyboard.is_pressed("right arrow") and meny_vald == 3:
            slutuppdrag.main()

        if __name__ == "__main__":
            main()












