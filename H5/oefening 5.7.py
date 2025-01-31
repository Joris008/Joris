def main():
    getal = float(input("geef een positief geheel getal"))
    while ongeldig(getal):
        print("Je kan enkele gehele getallen invoeren")
        getal = float(input("Geeft positief geheel getal"))
    print(getal)

def ongeldig(getal):
    if getal > 0 and getal % 1 == 0:
        status = False
    else:
        status = True

    return status


main()