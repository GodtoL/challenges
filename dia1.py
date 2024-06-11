# Challenge 1 - Invertir una cadena
def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])
    
result = reverse_string(input('Escribe una palabra: '))
print(result)
