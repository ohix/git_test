eingabe = input("Gebe deine Zahlenfolge ein: ")

case = 0
letzteZahl = False

for i in range(len(eingabe)):
    number = eingabe[i]
    if case == 0:
        if number == 0: case = 1
        elif i == len(eingabe)-1:
            letzteZahl = True
    elif case == 1:
        if number == 0: case = 2
        if number == 1: case = 0
    else:
        print("error")

if case == 0 and letzteZahl != True:
    print("Eingabe: ", eingabe + " TRUE")
else:
    print("Eingabe: ", eingabe + " FALSE")

#mir ist bewusst, dass es DEUTLICH kürzer geht, jedoch will ich das Automatenschemata eindeutig im Code sichbar machen
Der Begriff Binär bezeichnet nach DIN 44300 etwas, das zwei Zeichen annehmen kann.
Unter Dual versteht man ein Zahlensystem, das nur aus zwei Zeichen besteht.

Dualzahlen werden nach der gleichen Methode wie im Dezimalsystem addiert.
Die Zahlen werden untereinander geschrieben und spaltenweise addiert.
Im Dualsystem gilt 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1 und 1 + 1 = 0 mit dem Übertrag 1, der an die nächsthöhere Stelle weitergegeben wird.

Ein Binärcode besteht aus einer bestimmten Anzahl an Ziffern.
Der Code kann übersetzt werden, indem jede Ziffer multipliziert wird mit: 2 hoch der Position der Ziffer in der Ziffernfolge.
Diese Position beginnt jedoch bei 0 anstelle von 1 zu zählen und wird von rechts nach links gelesen.