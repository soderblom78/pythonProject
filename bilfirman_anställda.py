def main():

    # Bilfirman, anställd personal

    # Listor personal
    personal = []
    anställningsnummer = ["1", "2", "3", "4"]
    anställd_namn = ["Bengt", "Arne", "Gustav", "Mikael"]
    anställd_befattning = ["VD", "Verkstad", "Verkstad", "Säljare"]
    anställd_månadslön = ["45000", "32000", "32000", "34000"]

    # Funktion printa ut sammanställd personallista
    def personallista():
        antal_anställda = anställningsnummer[-1]
        print("Antal anställda: " + antal_anställda)
        print("\n" + "Anst.nr: " + anställningsnummer[0] + ","" Befattning: " + anställd_befattning[0] + "," + " Namn: "
              + anställd_namn[0] + "," + " Månadslön: " + anställd_månadslön[0])
        print("Anst.nr: " + anställningsnummer[1] + ","" Befattning: " + anställd_befattning[1] + "," + " Namn: "
              + anställd_namn[1] + "," + " Månadslön: " + anställd_månadslön[1])
        print("Anst.nr: " + anställningsnummer[2] + ","" Befattning: " + anställd_befattning[2] + "," + " Namn: "
              + anställd_namn[2] + "," + " Månadslön: " + anställd_månadslön[2])
        print("Anst.nr: " + anställningsnummer[3] + ","" Befattning: " + anställd_befattning[3] + "," + " Namn: "
              + anställd_namn[3] + "," + " Månadslön: " + anställd_månadslön[3])

    print("\nBILFIRMAN: PERSONAL\n")
    # Kallar på sammanställd personallista
    personallista()
    # Avslutningsfras
    input("\nTryck enter för att komma till huvudmeny!")

    if __name__ == "__main__":
        main()
