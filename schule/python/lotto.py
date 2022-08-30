#lotto
import random

nutzer_zahlen = [] #Liste für Benutzereingabe

for i in range(1,7):
    eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl ein: "))
    while eingabe in nutzer_zahlen or eingabe > 49:
        print("Falsche eingabe")
        eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl erneut ein: "))
    nutzer_zahlen.append(eingabe)


lottozahlen = [] #Liste für Lottozahlen

for i in range(6):
    zufallszahl = random.randint(1, 49) #aktuell gezogene Zahl
    if zufallszahl in lottozahlen: 
        continue
    lottozahlen.append(zufallszahl)


print ("Deine Zahlen: " + str(nutzer_zahlen))
print ("Lottozahlen: " + str(lottozahlen))


#Vergleich von Lottozahlen und Benutzereingabe
richtige = 0

for element in nutzer_zahlen:
    if element in lottozahlen:
        richtige+=1
        print(str(element) + " ist in den Lottozahlen enthalten.")
