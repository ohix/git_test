import random 

zahlen = list(range(1,49)) 
random.shuffle(zahlen) 
lotto_zahlen = zahlen[:6] 

nutzer_zahlen = [] 
    
for i in range(1,7): 
    eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl ein: ")) 
    while eingabe in nutzer_zahlen or eingabe > 49: 
        print("Falsche eingabe") 
        eingabe = int(input("Bitte geben Sie die " + str(i) + ". Zahl erneut ein: ")) 
    nutzer_zahlen.append(eingabe) 
    
print ("Deine Zahlen: " + str(nutzer_zahlen) + " | Lottozahlen: " + str(lotto_zahlen)) 

richtige = 0 
doppelte_zahlen = [] 

for zahl in nutzer_zahlen: 
    if zahl in lotto_zahlen:  
        doppelte_zahlen.append(zahl) 
        richtige+=1 

print("Doppelte Zahlen: " + str(doppelte_zahlen) + " | Anzahl der Dopplungen: " + str(richtige)) 