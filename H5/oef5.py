from mijn_module import*

def main():
    weerstand = int(input("De weerstand is: "))
    spanning = int(input("De spanning is: "))
    warmte = int(input("De warmte is: "))
    tijd = u_r_q_naar_t(spanning, weerstand, warmte)
    print("De tijd is", tijd)


main()