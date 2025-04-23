def main():
    prijs = haal_prijs()
    bedrag = haal_bedrag()
    if bedrag < prijs:
        print('Te weinig betaald.')
    else:
        wisselgeld = bedrag - prijs
        vijfeuro = wisselgeld // 5
        rest = wisselgeld % 5
        tweeeuro = rest / 2
        eeneuro = rest % 2


def valid_prijs():
    try:
        prijs = int(input("Wat is de prijs? "))
        return True
    except:
        print("De prijs moet aan volgende eisen voldoen")
        return False

def valid_bedrag():
    try:
        berdag = int(input("Wat is je bedrag? "))
        return True
    except:
        print("Het bedrag moet aan volgende eisen voldoen")
        return False

def haal_bedrag():
     bedrag = input("Wat is het bedrag? ")
    while not valid_bedrag(bedrag):
        print("Het bedrag is ongeldig")
        bedrag = input("Wat is het bedrag? ")
    return bedrag


def haal_prijs():
     prijs = input("Wat is de prijs? ")
    while not valid_prijs(prijs):
        print("De prijs is ongeldig")
        prijs = input("Wat is de prijs? ")
    return prijs


main()

