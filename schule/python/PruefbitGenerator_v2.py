eingabe = input("Gib eine Ziffernfolge (0,1) ein! ")
e = ''
a = ''
s = ''
case = 0

laenge = len(eingabe)
for i in range(laenge):
    e = eingabe[i]
    a = ''
    s = s+e
    if case == 0:
        if e == '0': case = 2
        if e == '1': case = 1
    elif case == 1:
        if e == '0': case = 3
        if e == '1': case = 4
    elif case == 2:
        if e == '0': case = 4
        if e == '1': case = 3
    elif case == 3:
        if e == '0': case = 0; a='1'; s=s+a
        if e == '1': case = 0; a='0'; s=s+a
    elif case == 4:
        if e == '0': case = 0; a='0'; s=s+a
        if e == '1': case = 0; a='1'; s=s+a
    print(str(case) + " | " + a + " | " + s)

print("Pruefbitfolge: ", s)