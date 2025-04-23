import random


def bestand_scorenboard_read():
    try:
        bestandsobject = open("scorenboard.txt", "r")
        score = [['', 0], ['', 0], ['', 0]]
        for i in range(3):
            score[i][0] = bestandsobject.readline().rstrip("\n")
            try:
                score[i][1] = int(bestandsobject.readline().rstrip("\n"))
            except ValueError:
                score[i][1] = 0
    bestandsobject.close()
    return score


def bestand_scorenboard_write(naam, score):
    print("U heeft de HIGHSCORE")
    bestandsobject = open("scorenboard.txt", "a")
    bestandsobject.write(naam + "\n")
    bestandsobject.write(str(score) + "\n")
    bestandsobject.close()


def bepaal_winnaar(computer, player):
    print("De computer koos:", computer)

    while computer == player:
        print("Gelijkspel! Probeer opnieuw")
        player = keuze_player()
        computer = keuze_computer()

    if (player == "blad" and computer == "steen") or \
            (player == "steen" and computer == "schaar") or \
            (player == "schaar" and computer == "blad"):
        print("Je wint")
        return 1
    else:
        print("De computer wint")
        return -1


def keuze_computer():
    return random.choice(["blad", "steen", "schaar"])


def keuze_player():
    player = input("Kies blad, steen of schaar: ")
    while player not in ["blad", "steen", "schaar"]:
        print("Ongeldige keuze!")
        player = input("Kies blad, steen of schaar: ")
    return player



def main():
    score = 0
    computer = keuze_computer()
    player = keuze_player()

    resultaat = bepaal_winnaar(computer, player)

    if resultaat == 1:
        score += 1
    elif resultaat == -1:
        print("Je hebt verloren. Eindscore:", score)
        return

    print("Huidige score:", score)


    scorelijst = bestand_scorenboard_read()


    if any(score > speler[1] for speler in scorelijst):
        print("U heeft een HIGHSORE")
        naam = input("Geef uw naam: ")
        bestand_scorenboard_write(naam, score)

    print("\n Highscores")
    scorelijst = bestand_scorenboard_read()
    for i, speler in scorelijst:
        print(f"{i + 1}. {speler[0]} - {speler[1]}")



main()
