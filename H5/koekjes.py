import time


def main():
    prijskoekjes = 3
    aantalkoekjes = 1
    print(aantalkoekjes," koekje(s) kost ",prijskoekjes, "euro")
    time.sleep(3)
    change_price(aantalkoekjes)

def change_price(aantalkoekjes):
    aantalkoekjes =  aantalkoekjes + 1
    prijskoekjes = 3 + aantalkoekjes
    print("vernader de prijs naar ",prijskoekjes, " Euro omdat het aantal koekjes is verandert naar", aantalkoekjes )

main()