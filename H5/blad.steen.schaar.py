import random  #Importeer een functie voor random

#Functie om het scoreboard in te lezen uit een bestand
def bestand_scorenboard_read():
    score = [['', 0], ['', 0], ['', 0]]  #Maak een lijst voor de top 3 scores (naam + score)
    try:
        bestandsobject = open("scorenboard.txt", "r")  #Probeer het bestand te openen om te lezen
        for i in range(3):  #Lees maximaal 3 scores
            score[i][0] = bestandsobject.readline().rstrip("\n")  #Lees naam
            try:
                score[i][1] = int(bestandsobject.readline().rstrip("\n"))  #Lees score
            except ValueError:
                score[i][1] = 0  #Als score geen getal is zet dan op 0
    except IOError:
        bestandsobject = open("scorenboard.txt", "w")  #Als bestand niet bestaat maak het dan aan

    bestandsobject.close()  #Sluit het bestand
    return score  #Stuur de scores terug


#Functie om een nieuwe score naar het scoreboardbestand te schrijven
def bestand_scorenboard_write(naam, score):
    #Lees de scores
    scorelijst = bestand_scorenboard_read()

    #Voeg de nieuwe score toe aan de lijst
    nieuwe_score = [naam, score]
    scorelijst.append(nieuwe_score)

    #Sorteer de scores van hoog naar laag
    gesorteerde_scores = []
    while scorelijst:
        hoogste = scorelijst[0]
        for speler in scorelijst:
            if speler[1] > hoogste[1]:  #Zoek speler met hoogste score
                hoogste = speler
        gesorteerde_scores.append(hoogste)  #Voeg hoogste score toe
        scorelijst.remove(hoogste)  #Verwijder hoogste score

    #Behoud enkel de top 3 scores
    top3 = gesorteerde_scores[:3]

    #Schrijf de top 3 naar het bestand
    bestand = open("scorenboard.txt", "w")
    for speler in top3:
        naam = speler[0]
        score = speler[1]
        bestand.write(naam + "\n")  #Schrijf naam naar bestand
        bestand.write(str(score) + "\n")  #Schrijf score naar bestand
    bestand.close()


#Functie om de winnaar te bepalen van het spel
def bepaal_winnaar(computer, player):
    print("De computer koos:", computer)
    #Controleer of het gelijkspel is
    while computer == player:
        print("Gelijkspel! Probeer opnieuw")
        player = keuze_player()  # Laat speler opnieuw kiezen
        computer = keuze_computer()  # Genereer nieuwe keuze voor computer

    #Controleer of de speler wint
    if (player == "blad" and computer == "steen") or \
       (player == "steen" and computer == "schaar") or \
       (player == "schaar" and computer == "blad"):
        print("Je wint")
        return 1  # peler wint
    else:
        print("De computer wint")
        return -1  #Computer wint


#Laat de computer random kiezen
def keuze_computer():
    return random.choice(["blad", "steen", "schaar"])


#Laat de player kiezen en controleer of het geldig is
def keuze_player():
    player = input("Kies blad, steen of schaar: ")
    while player not in ["blad", "steen", "schaar"]:  #Herhaal zolang invoer ongeldig is
        print("Ongeldige keuze!")
        player = input("Kies blad, steen of schaar: ")
    return player


#Het hoofdmenu van het spel
def main():
    score = 0  #Startscore
    while True:
        computer = keuze_computer()  #Ga naar functie voor het kiezen van de computers keuzen
        player = keuze_player()  #Ga naar de functie voor het kiezen van de players keuzen

        resultaat = bepaal_winnaar(computer, player)  #Bepaal de winnaar

        if resultaat == 1:
            score += 1  #Verhoog de score met 1 als de player wint
            print("Huidige score:", score)
        elif resultaat == -1:
            print("Je hebt verloren. Eindscore:", score)
            break  #Stop het spel als de player verliest

    #Lees het scoreboard
    scorelijst = bestand_scorenboard_read()

    #Controleer of het een highscore is
    if not scorelijst or score > min(speler[1] for speler in scorelijst):
        print("U heeft een HIGHSCORE")
        naam = input("Geef uw naam: ")  #Vraag naam van player
        bestand_scorenboard_write(naam, score)  #Schrijf score naar het bestand

    #Toon de highscores
    print("\nHighscores")
    scorelijst = bestand_scorenboard_read()
    for i, speler in enumerate(scorelijst):
        print(f"{i + 1}. {speler[0]} - {speler[1]}")  #Laat de naam en score zien


main()  #Start het spel
