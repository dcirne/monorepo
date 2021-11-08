#include "hanoi_solver.hpp"

#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
    unsigned int numberOfDisks = 3;

    if (argc > 1) {
        numberOfDisks = atoi(argv[1]);
    }

    std::cout << "\x1B[0;31mTower \x1B[0;32mof \x1B[0;34mHanoi\x1B[0m" << std::endl;
    TowerOfHanoi towerOfHanoi(numberOfDisks);
    towerOfHanoi.printState();
    towerOfHanoi.solve();
}
