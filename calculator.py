#Ask for user input
a = float(input("Type out first number: "))
b = input("Choose an arithmetic operator from +, -, * or /:")
c = float(input("Type out another number: "))

#Perform mathematical operation
if b == "+":
    answer = a + c
elif b == "-":
    answer = a - c
elif b == "*":
    answer = a * c
elif b == "/" and c != 0:
    answer = a / c
else:
    answer = "Invalid"

#Print out result
print(answer)