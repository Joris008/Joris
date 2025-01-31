import random


def keuze_computer():
    computer = random.choice(["blad", "steen", "schaar"])
    return computer


def keuze_player(computer):
    player = input("Kies blad, steen of schaar: ")
    if player not in ["blad", "steen", "schaar"]:
     print ("ongelidg antwoord")
    else:
        bepaal_winnaar(computer, player)



def bepaal_winnaar(computer, player):
    print("De computer koos: ", computer)
    if computer == player:
        print("gelijkspel")
    elif (player == "blad" and computer == "steen") or \
            (player == "steen" and computer == "schaar") or \
            (player == "schaar" and computer == "blad"):
        print("Je wint!")
    else:
        print("De computer wint")



def main():
    keuze_computer()
    computer = keuze_computer()
    keuze_player(computer)


while True:
    main()