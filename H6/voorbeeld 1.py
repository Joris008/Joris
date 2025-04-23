def wisselgeld():
    prijs = float(input("Productprijs: "))
    bedrag = float(input("Betaald bedrag: "))
    if bedrag < prijs:
        print('Te weinig betaald')
    else:
        vijfeuro = (bedrag - prijs) // 5
        if vijfeuro > 0:
            print('Betaal', vijfeuro, 'biljet(ten) van 5 euro')
        wissel = (bedrag - prijs) % 5
        tweeeuro = wissel // 2
        if tweeeuro > 0:
            print('Betaal', tweeeuro, 'munt(en) van 2 euro')
        eeneuro = wissel % 2
        print('Betaal', eeneuro, 'munt(en) van 1 euro')
    return bedrag - prijs

wisselgeld()
