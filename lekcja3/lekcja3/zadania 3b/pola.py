import globals
from pole_prostokata import ppp
from pole_trojkata import ppt


def pole_figury(nazwa):
    if nazwa == "prostokąt":
        return ppp(globals.a_prostokata, globals.b_prostokata)
    elif nazwa == "trójkąt":
        return ppt(globals.a_trojkata, globals.h_trojkata)
    elif nazwa == "kwadrat":
        return ppp(globals.a_kwadratu, globals.a_kwadratu)
    else:
        return "Error, brak figury w spisie."
