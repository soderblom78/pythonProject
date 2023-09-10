
# importerade filer, moduler
import roger2
import roger3
from os import system, name
import keyboard


# Funktion för att rensa skärmen
def clear():
    if name == "nt":
        _ = system("cls")


# variabel håller reda på vald meny (meny_vald +=1 eller meny_vald -=1)
meny_vald = 1

# variabel håller reda på vald undermeny (undermeny_vald +=1 eller undermeny_vald -=1)
undermeny_vald = 1

# While loop, kör programmet tills användaren väljer Avsluta i menyvalet
while True:
    # Rensar skärmen
    clear()
    # Hälsar användaren välkommen och ger info om menyvalen
    print("VÄLKOMMEN TILL KÖTTBUTIKEN")
    print("\nPlocka ihop en valfri köttlåda, gör så här:\n - välj med piltangenterna "
          "höger eller vänster valfritt djurslag, köttlåda eller avsluta.\n - Tryck sedan piltangent ned för att komma in i menyn\n")

    # Från modulen keyboard, registrerar vilken tangent på tangentbordet användaren har tryckt in.
    # Med villkorens hjälp testas vilken tangent användaren har tryckt ned, samt vilken meny eller
    # undermeny som är vald.
    # I det här fallet testas: Pil ned, Pil upp, Pil höger, Pil vänster
    if keyboard.is_pressed("right arrow") and meny_vald < 6 and undermeny_vald == 1:
        meny_vald += 1
    elif keyboard.is_pressed("left arrow") and meny_vald > 1 and undermeny_vald == 1:
        meny_vald -= 1
    elif keyboard.is_pressed("down arrow") and undermeny_vald < 5:
        undermeny_vald += 1
    elif keyboard.is_pressed("up arrow") and undermeny_vald > 1:
        undermeny_vald -= 1

    elif meny_vald == 1 and undermeny_vald == 1:
        meny1 = roger2.kött_1()

    elif meny_vald == 2 and undermeny_vald == 1:
        meny2 = roger2.kött_2()

    elif meny_vald == 3 and undermeny_vald == 1:
        meny3 = roger2.kött_3()

    elif meny_vald == 4 and undermeny_vald == 1:
        meny4 = roger2.kött_4()

    elif meny_vald == 5 and undermeny_vald == 1:
        meny5 = roger2.kött_5()

    elif meny_vald == 6 and undermeny_vald == 1:
        meny6 = roger2.kött_6()

    elif undermeny_vald == 2 and meny_vald == 1:
        meny = roger2.kött_1()

        undermeny = roger2.kött_låda()

    elif undermeny_vald == 2 and meny_vald == 2:
        meny = roger2.kött_2()

        undermeny = roger2.kött_nöt(3)
        detalj = roger3.oxfile()

    elif undermeny_vald == 3 and meny_vald == 2:
        meny = roger2.kött_2()

        undermeny = roger2.kött_nöt(2)
        detalj = roger3.fransyska()

    elif undermeny_vald == 4 and meny_vald == 2:
        meny = roger2.kött_2()

        undermeny = roger2.kött_nöt(1)
        detalj = roger3.lövbiff()

    elif undermeny_vald == 5 and meny_vald == 2:
        meny = roger2.kött_2()

        undermeny = roger2.kött_nöt(0)
        detalj = roger3.biff()

    elif undermeny_vald == 2 and meny_vald == 3:
        meny = roger2.kött_3()

        undermeny = roger2.kött_kalv(3)
        detalj = roger3.kalvkotlett()

    elif undermeny_vald == 3 and meny_vald == 3:
        meny = roger2.kött_3()

        undermeny = roger2.kött_kalv(2)
        detalj = roger3.kalvstek()

    elif undermeny_vald == 4 and meny_vald == 3:
        meny = roger2.kött_3()

        undermeny = roger2.kött_kalv(1)
        detalj = roger3.kalvschnitzel()

    elif undermeny_vald == 5 and meny_vald == 3:
        meny = roger2.kött_3()

        undermeny = roger2.kött_kalv(0)
        detalj = roger3.kalvfilé()

    elif undermeny_vald == 2 and meny_vald == 4:
        meny = roger2.kött_4()

        undermeny = roger2.kött_lamm(3)
        detalj = roger3.lammkotlett()

    elif undermeny_vald == 3 and meny_vald == 4:
        meny = roger2.kött_4()

        undermeny = roger2.kött_lamm(2)
        detalj = roger3.lammstek()

    elif undermeny_vald == 4 and meny_vald == 4:
        meny = roger2.kött_4()

        undermeny = roger2.kött_lamm(1)
        detalj = roger3.lammlägg()

    elif undermeny_vald == 5 and meny_vald == 4:
        meny = roger2.kött_4()

        undermeny = roger2.kött_lamm(0)
        detalj = roger3.lammfile()

    elif undermeny_vald == 2 and meny_vald == 5:
        meny = roger2.kött_5()

        undermeny = roger2.kött_gris(3)
        detalj = roger3.fläskkotlett()

    elif undermeny_vald == 3 and meny_vald == 5:
        meny = roger2.kött_5()

        undermeny = roger2.kött_gris(2)
        detalj = roger3.fläskkarre()

    elif undermeny_vald == 4 and meny_vald == 5:
        meny = roger2.kött_5()

        undermeny = roger2.kött_gris(1)
        detalj = roger3.skinkstek()

    elif undermeny_vald == 5 and meny_vald == 5:
        meny = roger2.kött_5()

        undermeny = roger2.kött_gris(0)
        detalj = roger3.revbensspjäll()

    elif undermeny_vald == 2 and meny_vald == 6:
        clear()
        meny = roger2.kött_avsluta()

    keyboard.read_key()

    if keyboard.is_pressed("right arrow") and undermeny_vald == 2 and meny_vald == 5:
        detalj_vald = roger2.s(15)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 3 and meny_vald == 5:
        detalj_vald = roger2.s(14)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 4 and meny_vald == 5:
        detalj_vald = roger2.s(13)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 5 and meny_vald == 5:
        detalj_vald = roger2.s(12)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 2 and meny_vald == 4:
        detalj_vald = roger2.s(11)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 3 and meny_vald == 4:
        detalj_vald = roger2.s(10)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 4 and meny_vald == 4:
        detalj_vald = roger2.s(9)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 5 and meny_vald == 4:
        detalj_vald = roger2.s(8)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 2 and meny_vald == 3:
        detalj_vald = roger2.s(7)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 3 and meny_vald == 3:
        detalj_vald = roger2.s(6)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 4 and meny_vald == 3:
        detalj_vald = roger2.s(5)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 5 and meny_vald == 3:
        detalj_vald = roger2.s(4)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 2 and meny_vald == 2:
        detalj_vald = roger2.s(3)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 3 and meny_vald == 2:
        detalj_vald = roger2.s(2)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 4 and meny_vald == 2:
        detalj_vald = roger2.s(1)

    elif keyboard.is_pressed("right arrow") and undermeny_vald == 5 and meny_vald == 2:
        detalj_vald = roger2.s(0)







