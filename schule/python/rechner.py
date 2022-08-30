first = int(input("Was ist deine erste Zahl? "))
operator = input("Was ist dein operator? ")
second = int(input("Was ist deine erste Zahl? "))

element = 0

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first/second)
elif operator == "/*":
    print(first//second)
    print("Rest:", first%second)
elif operator == "*":
    print(first*second)
else: 
    print("falsches Zeichen")