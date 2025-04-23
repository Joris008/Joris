bestandsobject = open("eenheidsmatrix.txt", "w")


for rij in range (4):
    for kol in range(4):
        if rij == kol:
            bestandsobject.write("1")
        else:
            bestandsobject.write("0")

    bestandsobject.write("\n")