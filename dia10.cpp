#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int intarray[5];
    int index = 0;
    int number;
    std::cout << "---Ordenando un array de 5 enteros---\n";

    do{
        std::cout << "Ingrese un numero entero: ";
        std::cin >> number;
        intarray[index] = number;
        index ++;

    }while(index < 5);
    
    std::sort(intarray, intarray + 5);

    for (int i = 0; i < 5; i++) {
        cout << intarray[i] << " ";
    }
    cout << endl;

    return 0;
}
