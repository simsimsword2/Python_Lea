import Methode
"""#Spiel Schere-Stein-Papier (oder auch Schnick-Schnack-Schnuck) stehen sich zwei"""
'#Spieler gegenüber und wählen gleichzeitig je eines von drei möglichen Handzeichen Schere,'
'#stein oder Papier'


runden = int(input("Wie viele Runden? "))

for i in range(0, runden):
    Methode.figur()
