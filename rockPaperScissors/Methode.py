import random

"""#Schreiben Sie eine Funktion, die mit derselben Wahrscheinlichkeit Schere, Stein oder"""
"#Papier zurückgibt. Die Funktion soll so oft aufgerufen werden, wie es Runden gibt."


def figur():
    mylist = ["Schere", "Stein", "Papier"]
    print(random.choice(mylist), end = ', ')
