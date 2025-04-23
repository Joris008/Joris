
def get_index():
    index = input ("Het hoeveelste getal wil je nog kennen")#Deze functie heeft geen runtime fouten
    while not valid(index):
        index = input("Het hoeveelste getal wil je nog kennen? ")
    return int(index)

def valid(index):
    try:
        index = int(index)
        if 1 <= index <= 5:
            return True
        else:
            print("Het getal moet tussen 1 en 5 zitten")
            return False
    except ValueError:
        print("ERROR")
        print("geef een getal in:")
        return False
    except:
        print("onbekende fout")
        return False


def grootste_getal():
    cijfers = [4, 8, 2, 9, 5]

    print("Het grootste getal is: ", max(cijfers))
    index = get_index()
    print("Het eerste element is: ", cijfers[index -1])


grootste_getal()
