# include <iostream>

int main(){
    int number1;
    int number2;
    int numbersum;
    std::cout << "----- Suma de numeros -----\n";
    std::cout << "Ingrese el primer numero: ";
    std::cin >> number1;
    std::cout << "Ingrese el segundo numero: ";
    std::cin >> number2;
    numbersum = number1 + number2;
    std::cout << "El resultado es: " << numbersum;

    return 0;
}