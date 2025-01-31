

def main():
    getal_1 = int(input("Geef een getal: "))
    print(getal_1)
    print("cm")
    getal_2 = omzetting(getal_1)
    print(getal_2)
    print("inch")

def omzetting(getal_1):
    getal_2 = getal_1 * 2,54
    return getal_2

main()