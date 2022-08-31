first = int(input("Was ist deine erste Zahl? "))
operator = input("Was ist dein Operator? ")
second = int(input("Was ist deine erste Zahl? "))

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