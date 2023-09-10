import slutuppdrag


def main():

    # Bilfirman

    # importerade moduler
    import datetime
    from datetime import date
    import keyboard
    from os import system, name
    import time

    # Funktion för att rensa skärmen
    def clear():
        if name == "nt":
            _ = system("cls")

    # Rensar skärmen vid start
    clear()

    # Skriver ut dagens datum och tid
    tid = datetime.datetime.now()
    print("Dagens datum och tid:", tid)

    # Sparar tid i string variabel
    tiden = ""
    tiden = str(tid)


    lagrat_namn = []
    lagrat_efternamn = []
    lagrat_personnummer_år = []
    lagrat_personnummer_månad = []
    lagrat_personnummer_dag = []
    lagrat_mail = []
    lagrat_telefon = []
    lagrat_uträknat_år = []

    # Funktion för personregistrering, kund
    def personregistrering():
        clear()
        namn = input("Förnamn: ")
        # Vilkoren testar om användaren skriver in uppgifterna för första gången eller om användaren
        # valt att ändra uppgifterna. Om användaren har valt att ändra uppgifterna gäller följande:
        # Ny uppgift - uppgiften kommer att ändras till det nya inmatade
        # Inte ny uppgift, användaren trycker förbi med Enter - Den gamla uppgiften kommer att vara kvar.
        if len(namn) > 0:
            lagrat_namn.append(namn)
        efternamn = input("Efternamn: ")
        if len(efternamn) > 0:
            lagrat_efternamn.append(efternamn)

        personnummer_år = input("Födelseår (fyra siffror): ")
        if len(personnummer_år) > 0:
            lagrat_personnummer_år.append(personnummer_år)
        personnummer_månad = input("Månad,(i siffror): ")
        if len(personnummer_månad) > 0:
            lagrat_personnummer_månad.append(personnummer_månad)
        personnummer_dag = input("Dag?: ")
        if len(personnummer_dag) > 0:
            lagrat_personnummer_dag.append(personnummer_dag)

        mail = input("Mailadress: ")
        if len(mail) > 0:
            lagrat_mail.append(mail)
        telefon = input("Telefonnummer: ")
        if len(telefon) > 0:
            lagrat_telefon.append(telefon)

        # Uträkning ålder (Ska användas främst för att se om kunden är över 18 år)
        today = date.today()
        år = today.strftime("%Y")
        idag_år = int(år)
        användare_år = int(lagrat_personnummer_år[-1])
        uträknat_år = idag_år-användare_år
        lagrat_uträknat_år.append(uträknat_år)

        månad = today.strftime("%m")
        idag_månad = int(månad)
        användare_månad = int(lagrat_personnummer_månad[-1])
        uträknat_månad = idag_månad-användare_månad

        dag = today.strftime("%d")
        idag_dag = int(dag)
        användare_dag = int(lagrat_personnummer_dag[-1])
        uträknat_dag = idag_dag - användare_dag

        # Drar bort en månad om dagen man fyller år är senare än dagens dag
        if uträknat_dag < 0:
            uträknat_månad -= 1

        # Drar bort ett år om månaden man fyller år är senare än nuvarande månad
        if uträknat_månad < 0:
            uträknat_år -= 1

    # Hälsar användaren välkommen
    input("\nHej och välkommen till Bilfirman! Som ny kund behöver vi era personuppgifter, tryck Enter!")
    # Kallar på funktionen personregistrering
    personregistrering()
    print("Tack så mycket!")
    # En liten fördröjning på 1 sekunder så att användaren hinner läsa Tack så mycket!
    time.sleep(1)

    # Meny 1-8 (varav 4 och 5 är undermenyer)
    def meny1():
        print("---> Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny2():
        print("Ändra dina personuppgifter")
        print("--->  Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny3():
        print("Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("--->  Bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny4():
        print("Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("--->  Begagnade bilar på lager")
        print("      Nya bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny5():
        print("Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("      Begagnade bilar på lager")
        print("--->  Nya bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny6():
        print("Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("--->  Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny7():
        print("Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("--->  Dina inköpta bilar")
        print("Avsluta, gå till huvudmeny")

    def meny8():
        print("Ändra dina personuppgifter")
        print("Sälj din bil, registrera ditt fordon här")
        print("Bilar på lager")
        print("Dina registrerade fordon som du vill sälja")
        print("Dina inköpta bilar")
        print("--->  Avsluta, gå till huvudmeny")

    # nya bilar på lager
    nya_bilar_lager = []
    ny_bil_1 = ["Ny bil 1.", "Mazda", "MX-30 e-SKYACTIV", "Årsmodell", "2021", "Miltal", "0-499"]
    ny_bil_2 = ["Ny bil 2.", "Suzuki", "Swace 1,8 inclusive CVT (122hk)", "Årsmodell", "2021", "Miltal", "0-499"]

    # begagnade bilar på lager
    begagnade_bilar_lager = []
    beg_bil_1 = ["Begagnad bil 1.", "Volvo", "V-40 D3 Momentum EURO 6 (150hk)", "Årsmodell", "2017", "Miltal", "7200"]
    beg_bil_2 = ["Begagnad bil 2.", "Peugeot", "2008 1,2 VTi Aut", "Årsmodell", "2017", "Miltal", "4360"]
    beg_bil_3 = ["Begagnad bil 3.", "Peugeot", "208 PureTech 5dr (82hk)", "Årsmodell", "2016", "Miltal", "8630"]
    beg_bil_4 = ["Begagnad bil 4.", "MINI Cooper", "D 1,6 (112hk)", "Årsmodell", "2012", "Miltal", "10199"]
    beg_bil_5 = ["Begagnad bil 5.", "Volvo", "V-40 T2 (122hk) Momentum", "Årsmodell", "2016", "Miltal", "9466"]
    beg_bil_6 = ["Begagnad bil 6.", "Hyundai", "Tucson 1,6 T-GDI 4WD (177hk)", "Årsmodell", "2018", "Miltal", "7404"]

    # Sparade listor

    # lista, kunden vill köpa dessa bilar
    köpta_bilar = []

    # lista, kunden vill sälja dessa bilar
    sålda_bilar = []


    # variabel för kundens registrerade fordon
    reg_fordon = 0

    # B = variabel för antal begagnade bilar som kunden vill köpa (köpt begagnad bil += 1)
    b = 0

    # n = variabel för antal nya bilar som kunden vill köpa (köpt ny bil += 1)
    n = 0

    # variabel håller reda på vald meny (meny_vald +=1 eller meny_vald -=1)
    meny_vald = 1

    # variabel håller reda på vald undermeny (undermeny_vald +=1 eller undermeny_vald -=1)
    undermeny_vald = 1

    # While loop, kör programmet tills användaren väljer Avsluta i menyvalet
    while True:
        clear()
        print("\nBILFIRMAN: FÖRSÄLJNING\n")
        print("\nGör ett val med piltangenterna upp eller ned. tryck HÖGER PIL för att välja!\n")

        # Från modulen keyboard, registrerar vilken tangent på tangentbordet användaren har tryckt in.
        # Med vilkorens hjälp testas vilken tangent användaren har tryckt ned, samt vilken meny eller
        # undermeny som är vald.
        # I det här fallet testas: Pil ned, Pil upp, Pil höger, Pil vänster
        if keyboard.is_pressed("down arrow") and meny_vald < 6 and undermeny_vald == 1:
            meny_vald += 1
        elif keyboard.is_pressed("up arrow") and meny_vald > 1 and undermeny_vald == 1:
            meny_vald -= 1
        elif keyboard.is_pressed("right arrow") and meny_vald == 3:
            undermeny_vald += 1
        elif keyboard.is_pressed("down arrow") and undermeny_vald < 3:
            undermeny_vald += 1
        elif keyboard.is_pressed("down arrow") and undermeny_vald == 3:
            undermeny_vald = 1
        elif keyboard.is_pressed("up arrow") and undermeny_vald > 1:
            undermeny_vald -= 1
        elif keyboard.is_pressed("left arrow"):
            undermeny_vald = 1

        elif meny_vald == 1:
            meny1()

        elif meny_vald == 2:
            meny2()

        elif meny_vald == 3 and undermeny_vald == 1:
            meny3()

        elif meny_vald == 3 and undermeny_vald == 2:
            meny4()

        elif meny_vald == 3 and undermeny_vald == 3:
            meny5()

        elif meny_vald == 4:
            meny6()

        elif meny_vald == 5:
            meny7()

        elif meny_vald == 6:
            meny8()

        # Från modulen keyboard, stoppar och läser av användarens tryckta tangent
        keyboard.read_key()

        # Vilkoret testar om användaren tryckt in Höger pil och att undermeny vald = 1 (det vill säga det
        # ursprungliga värdet som betyder att användaren inte är inne i någon undermeny)
        if keyboard.is_pressed("right arrow") and undermeny_vald == 1:

            # Om användaren tryckt Höger pil och meny vald = 1, dvs Ändra dina personuppgifter
            if meny_vald == 1:
                # Rensar skärmen
                clear()

                # Skriver ut vilken meny som är vald
                print("MENYVAL: ÄNDRA DINA PERSONUPPGIFTER")

                # Skriver ut tidigare inmatade personuppgifter av användaren
                print("\n Användare:\n " + lagrat_namn[-1] + " " + lagrat_efternamn[-1] +
                      "\n Ålder: " + str(lagrat_uträknat_år[-1]) + " år\n", "Mailadress: " +
                      lagrat_mail[-1] + "\n Telefonnummer: " + lagrat_telefon[-1])

                # Användaren får ett val att ändra sina personuppgifter eller att gå tillbaka till menyn
                ändra_personuppgifter = input(" \nVill du ändra skriv ändra, annars tryck enter för att komma tillbaka till menyn: ")
                if ändra_personuppgifter.casefold() == "ändra":
                    personregistrering()

            # Om användaren tryckt Höger pil och meny vald = 2, dvs Sälj din bil, registrera ditt fordon
            if meny_vald == 2:
                clear()
                print("MENYVAL: SÄLJ DIN BIL, REGISTRERA DITT FORDON")

                # insamlingsuppgifter, inköp av bilar
                bilmärke = input("\nVilket bilmärke har du?: ")

                modell = input("Vilken modellbeteckning?: ")

                årsmodell = input("Vilken årsmodell?: ")

                antal_kilometer = input("Hur långt har den gått?, antal kilometer: ")
                sålda_bilar.append(bilmärke + " " + modell + " årsmodell " + årsmodell + " " + antal_kilometer + " kilometer")

                # Sammanfattning
                print("\nOk, du säljer alltså en " + bilmärke, modell, "från " + årsmodell, "som har gått " + antal_kilometer,
                "kilometer, det låter intressant! Vi kommer att höra av oss till dig!")
                # Antal reg fordon
                reg_fordon += 1
                gå_vidare = input("Tryck enter för att komma tillbaks till meny")
                meny_vald = 1


            # Om användaren tryckt Höger pil och meny vald = 4, dvs Dina registrerade fordon
            if meny_vald == 4:
                clear()
                print("MENYVAL: DINA REGISTRERADE FORDON")

                # Vilkoren testar hur många fordon som registrerats genom värdet av reg_fordon
                # Är värdet oförändrat dvs 0, betyder det att användaren inte registrerat något fordon
                if reg_fordon == 0:
                    print("\nDu har inte registrerat något fordon")
                    gå_vidare = input("Tryck enter för att komma tillbaks till meny")

                elif reg_fordon == 1:
                    print("\nDu har", reg_fordon, "registrerat fordon")
                    print("\n".join(map(str, sålda_bilar)))
                    gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

                else:
                    print("\nDu har", reg_fordon, "registrerade fordon")
                    print("\n".join(map(str, sålda_bilar)))
                    gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

                    # Återställer värdet på meny vald till 1
                    meny_vald = 1

            # Om användaren tryckt Höger pil och meny vald = 5, dvs Dina inköpta bilar
            if meny_vald == 5:
                clear()
                print("MENYVAL: DINA INKÖPTA BILAR")

                # Vilkoren testar hur många bilar som användaren köpt in genom att mäta längden av
                # innehållet i variabeln köpta_bilar
                # Är innehållet tomt, betyder det att användaren inte köpt någon bil
                if len(köpta_bilar) == 0:
                    print("\nDu har inte köpt in någon bil")
                    gå_vidare = input("Tryck enter för att komma tillbaks till meny")
                    meny_vald = 1

                else:
                    # Om innehållet inte är tomt, betyder det att användaren har köpt någon bil.
                    # Värdet av antalet poster motsvarar antal köpta bilar som sedan printas ut till användaren.
                    print("\nDu har köpt", len(köpta_bilar), "fordon")
                    print("\n".join(map(str, köpta_bilar)))
                    gå_vidare = input("\nTryck enter för att komma tillbaks till meny")
                    meny_vald = 1

            # Om användaren tryck enter och meny vald = 6, dvs Avsluta, gå till huvudmeny
            # Samlad information om personuppgifter och biluppgifter skickas till en txt.fil
            if meny_vald == 6:
                with open("bilfirman_försäljning.txt", "a") as f:
                    f.write("\n")
                    f.write(tiden)
                    f.writelines("\n\n")
                    f.writelines("\n".join(lagrat_namn + lagrat_efternamn + lagrat_telefon + lagrat_mail))
                    f.write("\n")
                    f.write("\nSålda bilar\n")
                    f.writelines("\n".join(köpta_bilar))
                    f.write("\n")
                    f.write("\nBilar att köpa in?\n")
                    f.writelines("\n".join(sålda_bilar))
                    f.write("\n")

                slutuppdrag.main()

        # Om användaren tryck enter och undermeny vald = 2, Begagnade bilar på lager
        if keyboard.is_pressed("right arrow") and undermeny_vald == 2:
            clear()

            # Printar ut en lista på begagnade bilar som finns på lager
            while b < 6:
                clear()
                print("MENYVAL: BEGAGNADE BILAR PÅ LAGER")
                print("\nBegagnade bilar på lager:")
                print(" ".join(beg_bil_1))
                print(' '.join(beg_bil_2))
                print(" ".join(beg_bil_3))
                print(' '.join(beg_bil_4))
                print(" ".join(beg_bil_5))
                print(' '.join(beg_bil_6))

                # Ber användaren skriva in en siffra för att köpa bil eller
                # skriva klar för att återgå till menyn.
                beg_bil = input("\nSkriv in siffra (1-6) för köpa bil, eller klar för att återgå till menyn: \n")

                # Använder vilkor för att testa vilken siffra som matats in och vilken bil som valts.
                # När bilen köpts in förs den över till variabeln köpta bilar och formateras om från
                # list format till string format. Sedan raderas innehållet i variabeln
                # begagnad bil + (siffran på den bil som valts)
                if beg_bil == "1" and len(beg_bil_1) > 0:
                    köpta_bilar.append(" ".join(beg_bil_1))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(beg_bil_1[1:-2]) + "\nTryck enter!")
                    b += 1
                    beg_bil_1.clear()
                elif beg_bil == "2" and len(beg_bil_2) > 0:
                    köpta_bilar.append(" ".join(beg_bil_2))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(beg_bil_2[1:-2]) + "\nTryck enter!")
                    b += 1
                    beg_bil_2.clear()
                elif beg_bil == "3" and len(beg_bil_3) > 0:
                    köpta_bilar.append(" ".join(beg_bil_3))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(beg_bil_3[1:-2]) + "\nTryck enter!")
                    b += 1
                    beg_bil_3.clear()
                elif beg_bil == "4" and len(beg_bil_4) > 0:
                    köpta_bilar.append(" ".join(beg_bil_4))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(beg_bil_4[1:-2]) + "\nTryck enter!")
                    b += 1
                    beg_bil_4.clear()
                elif beg_bil == "5" and len(beg_bil_5) > 0:
                    köpta_bilar.append(" ".join(beg_bil_5))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(beg_bil_5[1:-2]) + "\nTryck enter!")
                    b += 1
                    beg_bil_5.clear()
                elif beg_bil == "6" and len(beg_bil_6) > 0:
                    köpta_bilar.append(" ".join(beg_bil_6))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(beg_bil_6[1:-2]) + "\nTryck enter!")
                    b += 1
                    beg_bil_6.clear()
                elif beg_bil == "klar" or b > 5:

                    break
                else:
                    # Om användaren matat in fel uppgifter skickas man tillbaka för ett nytt försök
                    input("Fel inmatning, försök igen! Tryck Enter")

            meny_vald = 1
            undermeny_vald = 1

        # Om användaren tryck enter och undermeny vald = 3, Nya bilar på lager
        if keyboard.is_pressed("right arrow") and undermeny_vald == 3:
            clear()

            while n < 2:
                clear()
                # Printar ut en lista på begagnade bilar som finns på lager
                print("MENYVAL: NYA BILAR PÅ LAGER")
                print("\nNya bilar på lager:")
                print(" ".join(ny_bil_1))
                print(' '.join(ny_bil_2))

                # Ber användaren skriva in en siffra för att köpa bil eller
                # skriva klar för att återgå till menyn.
                ny_bil = input("\nSkriv in siffra (1-2) för köpa bil, eller klar för att återgå till menyn: \n")

                if ny_bil == "klar":

                    break

                # Använder vilkor för att testa vilken siffra som matats in och vilken bil som valts.
                # När bilen köpts in förs den över till variabeln köpta bilar och formateras om från
                # list format till string format. Sedan raderas innehållet i variabeln
                # ny bil + (siffran på den bil som valts)
                elif ny_bil == "1" and len(ny_bil_1) > 0:
                    köpta_bilar.append(" ".join(ny_bil_1))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(ny_bil_1[1:-2]) + "\nTryck enter!")
                    n += 1
                    ny_bil_1.clear()
                elif ny_bil == "2" and len(ny_bil_2) > 0:
                    köpta_bilar.append(" ".join(ny_bil_2))
                    input("\nBra val! Vi kommer att reservera vald bil till dig:\n" +
                          " ".join(ny_bil_2[1:-2]) + "\nTryck enter!")
                    n += 1
                    ny_bil_2.clear()
                else:
                    print("Fel inmatning, försök igen!")

            meny_vald = 1
            undermeny_vald = 1

        if __name__ == "__main__":
            main()










