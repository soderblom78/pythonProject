# bilhandel AB


# insamlingsuppgifter, inköp av bilar
bilmärke = input("Vilket bilmärke har du?: ")
modell = input("Vilken modellbeteckning?: ")
årsmodell = input("Vilken årsmodell?: ")
antal_kilometer = input("Hur långt har den gått?, antal kilometer: ")

# Sammanfattning
print("Ok, du säljer alltså en " + bilmärke, modell, "från " + årsmodell, "som inte gått mer än " + antal_kilometer,
      "kilometer, det låter intressant!")



# lager
mitt_lager = []
bil_1 = ["1.", "Mazda", "MX-30 e-SKYACTIV", "Årsmodell", "2021", "Miltal", "0-499"]
bil_2 = ["2.", "Suzuki", "Swace 1,8 inclusive CVT (122hk)", "Årsmodell", "2021", "Miltal", "0-499"]
bil_3 = ["3.", "Volvo", "V-40 D3 Momentum EURO 6 (150hk)", "Årsmodell", "2017", "Miltal", "7200"]
bil_4 = ["4.", "Peugeot", "2008 1,2 VTi Aut", "Årsmodell", "2017", "Miltal", "4360"]
bil_5 = ["5.", "Peugeot", "208 PureTech 5dr (82hk)", "Årsmodell", "2016", "Miltal", "8630"]
bil_6 = ["6.", "MINI Cooper", "D 1,6 (112hk)", "Årsmodell", "2012", "Miltal", "10199"]
bil_7 = ["7.", "Volvo", "V-40 T2 (122hk) Momentum", "Årsmodell", "2016", "Miltal", "9466"]
bil_8 = ["8.", "Hyundai", "Tucson 1,6 T-GDI 4WD (177hk)", "Årsmodell", "2018", "Miltal", "7404"]

# Skriver ut en lista på lagerbilar
print()
print("-------------------------------------------------------------------------------------------------")
print("Hej och välkommen till min bilhall, här är det jag har inne just nu:")
print()
print(" ".join(bil_1))
print(' '.join(bil_2))
print(' '.join(bil_3))
print(' '.join(bil_4))
print(' '.join(bil_5))
print(' '.join(bil_6))
print(' '.join(bil_7))
print(' '.join(bil_8))

print("\nNu förstår jag att du är väldigt sugen på att handla in lite bilar.")
# kunden väljer vilka bilar som ska köpas in
handla_1 = input("\nSkriv in bilmärke, bilmodell, årsmodell, antal mil: ")
print("1. Vald bil: " + handla_1)
handla_2 = input("\nSkriv in bilmärke, bilmodell, årsmodell, antal mil: ")
print("2. Vald bil: " + handla_2)
handla_3 = input("\nSkriv in bilmärke, bilmodell, årsmodell, antal mil: ")
print("3. Vald bil: " + handla_3)
handla_4 = input("\nSkriv in bilmärke, bilmodell, årsmodell, antal mil: ")
print("4. Vald bil: " + handla_4)
print()
# kunden får ut en lista på vilka bilar som handlats
print("Här är en lista på vad du handlat för bilar idag:")
print(handla_1, handla_2, handla_3, handla_4, sep="\n")
print("\nTack och välkommen åter!")
