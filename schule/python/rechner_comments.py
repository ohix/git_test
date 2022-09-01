first = int(input("Was ist deine erste Zahl? ")) #Eingabe für erste Zahl
operator = input("Was ist dein Operator? ") #Eingabe für Operator
second = int(input("Was ist deine erste Zahl? ")) #Eingabe für zweite Zahl

if operator == "+": #Falls Operator + ist
    print(first + second) #Ergebnis ausgeben
elif operator == "-": #Falls Operator - ist
    print(first - second) #Ergebnis ausgeben
elif operator == "/": #Falls Operator / ist
    print(first/second) #Ergebnis ausgeben
elif operator == "/*": #Falls Operator // ist
    print(first//second) #Ergebnis, gibt den ganzahligen Teil der Division aus
    print("Rest:", first%second) #Rest ausgeben
elif operator == "*": #Falls Operator * ist
    print(first*second) #Ergebnis ausgeben
else: 
    print("falsches Zeichen") #Fehlermeldung ausgeben