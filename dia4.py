user_list = []

while True:
    user_number = int(input("Ingrese un número o escriba 0 para salir: "))
    if user_number == 0:
        break
    user_list.append(user_number)
    
user_list.sort()
print(user_list)