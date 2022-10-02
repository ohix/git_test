eingabe = input("Eingabe: ")
e = ''
a = ''
s = ''
case = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = ['er', 'sie', 'es']
words_in_eingabe = any(word in eingabe for word in words)

status = False

for i in range(len(eingabe)):
    if case == 0:
        if eingabe[i] in alphabet: case = 0
        if words_in_eingabe == True: case = 1; 
    elif case == 1:
        status = True
        if eingabe[i] in alphabet: case = 1

if status == True:
    print("Die Eingabe ist gültig.")
else:
    print("Die Eingabe ist ungültig.")