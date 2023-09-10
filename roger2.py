# importerad modul
import time

# Listor

köttlåda_pris = []
köttlåda_total = []
detalj_vikt = []

köttlåda = ["|KÖTTLÅDA|", " KÖTTLÅDA "]

nöt = ["|NÖT|", " NÖT ", "Oxfilé".rjust(27), "Fransyska".rjust(30), "Lövbiff".rjust(28), "Biff".rjust(25)]
nöt_detaljpris = [560, 114.95, 199.95, 244.95]

kalv = ["|KALV|", " KALV ", "Kalvkotlett".rjust(47), "Kalvstek".rjust(44), "Kalvschnitzel".rjust(49), "Kalvfilé".rjust(44)]
kalv_detaljpris = [239.95, 194.95, 249.90, 659.90]

lamm = ["|LAMM|", " LAMM ", "Lammkotlett".rjust(63), "Lammstek".rjust(60), "Lammlägg".rjust(60), "Lammfilé".rjust(60)]
lamm_detaljpris = [294.0, 214.90, 129.90, 699.00]

gris = ["|GRIS|", " GRIS ", "Fläskkotlett".rjust(80), "Fläskkarré".rjust(78), "Skinka".rjust(74), "Revbensspjäll".rjust(81)]
gris_detaljpris = [94.95, 94.95, 79.90, 59.90]

avsluta = ["|AVSLUTA|", " AVSLUTA "]

uppgifter = ["Namn: ", "Adress: ", "Telefon: ", "Mail: "]


# Menyer, högerjusterade
def kött_1():
    print(köttlåda[0], nöt[1].rjust(15), kalv[1].rjust(15), lamm[1].rjust(15), gris[1].rjust(15), avsluta[1].rjust(15))


def kött_2():
    print(köttlåda[1], nöt[0].rjust(15), kalv[1].rjust(15), lamm[1].rjust(15), gris[1].rjust(15), avsluta[1].rjust(15))


def kött_3():
    print(köttlåda[1], nöt[1].rjust(15), kalv[0].rjust(15), lamm[1].rjust(15), gris[1].rjust(15), avsluta[1].rjust(15))


def kött_4():
    print(köttlåda[1], nöt[1].rjust(15), kalv[1].rjust(15), lamm[0].rjust(15), gris[1].rjust(15), avsluta[1].rjust(15))


def kött_5():
    print(köttlåda[1], nöt[1].rjust(15), kalv[1].rjust(15), lamm[1].rjust(15), gris[0].rjust(15), avsluta[1].rjust(15))


def kött_6():
    print(köttlåda[1], nöt[1].rjust(15), kalv[1].rjust(15), lamm[1].rjust(15), gris[1].rjust(15), avsluta[0].rjust(15))


# Menyval köttlåda
def kött_låda():
    print("Lådan innehåller:")

    # värdet av x blir lika med antal priser som lagts till i listan köttlåda_pris
    x = len(köttlåda_pris)
    # värdet av a (detalj_vikt) = 0
    a = 0
    # värdet av k (köttlåda) = 2 eftersom de två första platserna (0 och 1) är menyval
    k = 2

    # Kör loopen så länge x > 0
    while x > 0:
        # printar ut detaljens vikt, detalj och pris
        print(detalj_vikt[a], "kg", köttlåda[k].strip(), "för", köttlåda_pris[a], "kr!")
        # minskar x med 1 för varje detaljpris som finns i listan
        x -= 1
        # ökar a med 1 för varje vikt som läggs till från listan
        a += 1
        # ökar k med 1 för varje detalj som läggs till från listan
        k += 1

    # Summerar och skriver ut köttlådans totala pris, avrundat till 2 decimaler
    summa = sum(köttlåda_pris).__round__(2)
    print("\nPris köttlåda:", summa, "kr")


# menyval. printar ut detalj för detalj som finns i aktuell lista. x bestämmer vilken detalj som
# ska vara markerad med pil. pilen är högerjusterad så därför måste jag ta bort den förinställda
# högerhusteringen på detaljerna med hjälp av item.strip()
def kött_nöt(x):
    for item in nöt[2:]:
        if x == 3:
            print("--->".rjust(25), item.strip())
        else:
            print(item)
        x += 1


def kött_kalv(x):
    for item in kalv[2:]:
        if x == 3:
            print("--->".rjust(40), item.strip())
        else:
            print(item)
        x += 1


def kött_lamm(x):
    for item in lamm[2:]:
        if x == 3:
            print("--->".rjust(56), item.strip())
        else:
            print(item)
        x += 1


def kött_gris(x):
    for item in gris[2:]:
        if x == 3:
            print("--->".rjust(72), item.strip())
        else:
            print(item)
        x += 1


# menyval avsluta
def kött_avsluta():
    if len(köttlåda) > 2:
        kött_låda()
        användare = []
        print("\nTack så mycket för din beställning! Skriv dina uppgifter nedan så "
              "kontaktar vi dig för en utkörning!\n")
        for i in uppgifter:
            a = input(i)
            användare.append(a)

        print("\nTack " + användare[0] + ", ha en jättefin dag!")
    else:
        print("Det blev inte något inköp idag, tack för visat intresse och välkommen åter!")

    time.sleep(2)
    quit()


# vald detalj, värdet av x håller reda på vilken detalj som är vald
def s(x):
    # defenierade variablar
    detalj = ""
    pris = ""

    # testar vilken detalj som är vald
    if x == 15:
        # tilldelar variabeln den aktuella detaljen för senare utskrift
        detalj = gris[2]
        # tilldelar variabeln det aktuella detaljpriset för senare beräkning
        pris = gris_detaljpris[0]

    elif x == 14:
        detalj = gris[3]
        pris = gris_detaljpris[1]

    elif x == 13:
        detalj = gris[4]
        pris = gris_detaljpris[2]

    elif x == 12:
        detalj = gris[5]
        pris = gris_detaljpris[3]

    elif x == 11:
        detalj = lamm[2]
        pris = lamm_detaljpris[0]

    elif x == 10:
        detalj = lamm[3]
        pris = lamm_detaljpris[1]

    elif x == 9:
        detalj = lamm[4]
        pris = lamm_detaljpris[2]
        köttlåda.append(lamm[4])

    elif x == 8:
        detalj = lamm[5]
        pris = lamm_detaljpris[3]

    elif x == 7:
        detalj = kalv[2]
        pris = kalv_detaljpris[0]

    elif x == 6:
        detalj = kalv[3]
        pris = kalv_detaljpris[1]

    elif x == 5:
        detalj = kalv[4]
        pris = kalv_detaljpris[2]

    elif x == 4:
        detalj = kalv[5]
        pris = kalv_detaljpris[3]

    elif x == 3:
        detalj = nöt[2]
        pris = nöt_detaljpris[0]

    elif x == 2:
        detalj = nöt[3]
        pris = nöt_detaljpris[1]

    elif x == 1:
        detalj = nöt[4]
        pris = nöt_detaljpris[2]

    elif x == 0:
        detalj = nöt[5]
        pris = nöt_detaljpris[3]

    # en loop körs för att testa att användaren har angett vikten i siffror samt att
    # vikten inte är 0 eller mindre.
    while True:
        print("Skriv in valfi vikt, tänk på att tecknet , skriver du med tecknet . och om du"
              "\nskriver 0 kommer inte detaljen räknas som inköpt")
        antal_kg = input("\nHur många kg " + detalj.strip() + " vill du ha?: ")

        try:
            antal_kg = float(antal_kg)
        except ValueError:
            print("Kan du skriva det i siffror tack!")
            time.sleep(2)
        else:
            antal_kg = float(antal_kg)
            pris = float(pris)
            summa = (pris * float(antal_kg)).__round__(2)
            if antal_kg > 0:
                print(antal_kg, "kg", detalj.strip(),  "för totalt:", summa, "kr stoppas i lådan")

                köttlåda_pris.append(summa)
                detalj_vikt.append(antal_kg)
                köttlåda.append(detalj)
                time.sleep(5)
            else:
                print("Vikten måste vara mer än 0 kg!")
                time.sleep(2)
                break
        break











