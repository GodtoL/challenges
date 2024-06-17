dictionar_user = {}
product_list = []
code_product_list = []

while True:
    product = input("Ingrese el nombre del producto o escriba F para finalizar: ")
    product = product.upper()
    if product == "F":
        break
    code_product = int(input("Ingrese el código del producto: "))
    product_list.append(product)
    code_product_list.append(code_product)

for prod in product_list:
    for value in code_product_list:
        dictionar_user[prod] = value

print(dictionar_user)
    