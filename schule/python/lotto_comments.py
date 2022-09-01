#lotto
import random

nutzer_zahlen = [] #Liste für Benutzereingabe

for i in range(1,7): #1 bis 6 (7 nicht inklusive)
    eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl ein: ")) # enutzereingabe
    while eingabe in nutzer_zahlen or eingabe > 49: #Fall Eingabe schon vorhanden oder größer als 49
        print("Falsche eingabe") #Fehlermeldung
        eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl erneut ein: ")) #Neue Eingabe
    nutzer_zahlen.append(eingabe) #Eingabe in Liste speichern


lottozahlen = [] #Liste für Lottozahlen

while len(lottozahlen) < 7: #Solange die Lottozahlen nicht 7 Elemente haben
    zufallszahl = random.randint(1, 49) #aktuell gezogene Zahl
    if zufallszahl in lottozahlen: #Falls Zahl in Liste vorhanden
        continue #gehe zu Beginn der Schleife
    lottozahlen.append(zufallszahl) #Zahl in Liste speichern


print ("Deine Zahlen: " + str(nutzer_zahlen)) #Ausgabe
print ("Lottozahlen: " + str(lottozahlen)) #Ausgabe


#Vergleich von Lottozahlen und Benutzereingabe

richtige = 0#Anzahl der richtigen Zahlen initialisieren

for element in nutzer_zahlen: #Für jedes Element in der Liste der Benutzereingaben
    if element in lottozahlen: #Falls Element in der Liste der Lottozahlen vorhanden
        richtige+=1 #Anzahl der richtigen Zahlen um 1 erhöhen
        print(str(element) + " ist in den Lottozahlen enthalten." + " Du hast " + str(richtige) + " Richtige.") #Ausgabe