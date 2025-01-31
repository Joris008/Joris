def stroom_berekenen(spanning, weerstand):
    stroom = spanning * weerstand
    return stroom

def vermogen_berekenen(stroom, weerstand):
    vermogen= stroom**2 * weerstand
    return vermogen

def tijd_berkenen(warmte, vermogen):
    tijd = warmte / vermogen
    return tijd

def u_r_q_naar_t(spanning, weerstand, warmte):
    stroom = stroom_berekenen(spanning, weerstand)
    vermogen = vermogen_berekenen(stroom, weerstand)
    tijd = tijd_berkenen(warmte, vermogen)
    return tijd
