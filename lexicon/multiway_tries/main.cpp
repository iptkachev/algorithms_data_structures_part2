#include <iostream>
#include "tree.hpp"

int main() {
    MultiwayTrie mTree;
    mTree.insert("test");
    std::cout << mTree.find("test") << "\n";
    std::cout << mTree.find("te") << "\n";
    mTree.insert("te");
    std::cout << mTree.find("te") << "\n";
    mTree.remove("test");
    std::cout << mTree.find("test") << "\n";
    return 0;
}