
def get_leeftijd():
    leeftijd = int(input("Wat is je leeftijd? "))
    while not valid_leeftijd(leeftijd):
        print("De leeftijd is ongeldig")
        leeftijd =input("Wat is je leeftijd? ")
    return leeftijd



def get_naam():
    naam = input("Wat is je naam? ")
    while not valid_naam(naam):
        print("De naam is ongeldig")
        naam = input("Wat is je naam? ")
    return naam



def valid_naam(naam):



def valid_leeftijd(leeftijd):
    try:
        leeftijd = bytes(input("Wat is je leeftijd? "))
        return True
    except:
        print("De leeftijd moet aan volgende eisen voldoen")
        return False


def verwerk_naam():
    naam = get_naam()
    leeftijd = get_leeftijd()
    if leeftijd >= 18:
        print("Welkom", naam, " je bent meerder jarig.")
    else:
        print("Je bent nog minderjarig, vraag toestemming aan een meerderjarige.")

        print("Je naam is ", len(naam), " letters lang.")



verwerk_naam()