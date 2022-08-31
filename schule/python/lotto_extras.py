import random #random Modul importieren

zahlen = list(range(1,49)) #Liste für Zahlen von 1 bis 49
random.shuffle(zahlen) #Liste zufällig mischen | Fisher–Yates shuffle | https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
lotto_zahlen = zahlen[:6] #Liste der ersten 6 Zahlen

nutzer_zahlen = [] #Liste für Benutzereingabe
    
for i in range(1,7): # 1 bis 6 (7 nicht inklusive)
    eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl ein: ")) # enutzereingabe
    while eingabe in nutzer_zahlen or eingabe > 49: #Falls Eingabe schon vorhanden oder größer als 49 | (while isinstance(int(eingabe), int) == True and eingabe in nutzer_zahlen or eingabe > 49)
        print("Falsche eingabe") #Fehlermeldung
        eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl erneut ein: ")) #Neue Eingabe
    nutzer_zahlen.append(eingabe) #Eingabe in Liste speichern
    
print ("Deine Zahlen: " + str(nutzer_zahlen) + " | Lottozahlen: " + str(lotto_zahlen)) # Ausgabe

richtige = 0 # Anzahl der richtigen Zahlen initialisieren
doppelte_zahlen = [] # Liste für doppelte Zahlen initialisieren

for zahl in nutzer_zahlen: #Für jede Zahl in der Liste der Benutzereingaben
    if zahl in lotto_zahlen:  #Falls Zahl in der Liste der Lottozahlen vorhanden
        doppelte_zahlen.append(zahl) #Zahl in Liste der doppelten Zahlen speichern
        richtige+=1 #Anzahl der richtigen Zahlen um 1 erhöhen

print("Doppelte Zahlen: " + str(doppelte_zahlen) + " | Anzahl der Dopplungen: " + str(richtige)) #Ausgabe