
def main():
    usefull_power = 30
    i = 1.5
    u = 24
    totale_power = calc_elektric_power(u, i)
    print("totale vermogen: ", totale_power,"W")
    rendement = calc_efficiency(totale_power, usefull_power)
    print("Het rendement: ", rendement,"%")


def calc_elektric_power(u, i):
    totale_power = u * i
    return totale_power


def calc_efficiency(totale_power, usefull_power ):
    rendement = (usefull_power/ totale_power)* 100
    return rendement



main()