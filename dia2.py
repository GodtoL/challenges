def multiply_number(number):
    for i in range(11):
        multiply = number * i
        print(f"{number} x {i} = {multiply}" )

number = int(input("Ingrese el numero que desea su tabla: "))
multiply_number(number)
