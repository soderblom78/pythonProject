# Bilfirman

# Personregistrering, användare
print("\nHej och välkommen till Bilfirman! Som ny användare behöver vi era personuppgifter")

förnamn = input("Förnamn: ")
efternamn = input("Efternamn: ")


# Meny med flera olika val
def meny():
    print("\n************************MENY************************")
    print("P. Ändra dina personuppgifter")
    print("\nA. Sälj din bil, registrera ditt fordon här")
    print("B. Begagnade bilar på lager")
    print("C. Nya bilar på lager")
    print("D. Dina registrerade fordon som du vill sälja")
    print("E. Dina inköpta bilar")
    print("F. Avsluta")


# En loop som körs tills man väljer att avsluta genom att välja menyval F (Avsluta)
while meny != "f":
    meny()
    menyval = input("\nVälj en bokstav A-F eller P för att ändra dina personuppgifter: ")

    # Menyval A - Insamlingsuppgifter, inköp av bilar
    if menyval.casefold() == "a":
        print("Här kan du sälja din bil")
        gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

    # Menyval B - Begagnade bilar på lager
    elif menyval.casefold() == "b":
        print("Här kan du se vilka begagnade bilar som finns på lager")
        gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

    # Menyval C - Nya bilar på lager
    elif menyval.casefold() == "c":
        print("Här kan du se vilka nya bilar som finns på lager")
        gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

    # Menyval D - Dina registrerade fordon som du vill sälja
    elif menyval.casefold() == "d":
        print("Här kan du se ditt eller dina fordon som du vill sälja")
        gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

    # Menyval E - Dina inköpta fordon
    elif menyval.casefold() == "e":
        print("Här kan du se ditt eller dina fordon som du köpt")
        gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

    # Menyval P - Ändra dina personuppgifter
    elif menyval.casefold() == "p":
        print("Här kan du ändra dina personuppgifter")
        gå_vidare = input("\nTryck enter för att komma tillbaks till meny")

    # Menyval F - Avsluta
    elif menyval.casefold() == "f":
        quit()

    # Fel menyval
    else:
        fel_menyval = input("Fel menyval, tryck enter för att återgå till meny: ")
