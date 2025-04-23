def bereken_gemiddelde():
    try:
        getal1 = int(input("Geef het eerste getal: "))
        getal2 = int(input("Geef het tweede getal: "))
        getal3 = int(input("Geef het derde getal: "))

        totaal = getal1 + getal2 + getal3
        gemiddelde = totaal / 3

        print("Het gemiddelde is:", gemiddelde)
    except ValueError:
        print("Het getal is incorrect")
        bereken_gemiddelde()

bereken_gemiddelde()
