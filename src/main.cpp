//
// Created by Alistaire Noiprasit on 29/8/2025.
// Edited by Alistaire Noiprasit 2/9/2025
//
#include "../include/AdvancedMath.h"
#include "../include/MathUtils.h"
#include <iostream>

int main() {

    // Modify as necessary
    int a = 3;
    int b = 4;
    int add_result = MathUtils::add(a, b);
    int multiply_result = MathUtils::multiply(a, b);
    int square_result = AdvancedMath::square(a);

    using namespace std;
    cout << "a + b = " << add_result << endl;
    cout << "a * b = " << multiply_result << endl;
    cout << "square(a) = " << square_result << endl;

    return 0;
}
