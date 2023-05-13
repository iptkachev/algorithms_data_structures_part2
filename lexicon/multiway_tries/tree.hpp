#pragma once
#include "node.hpp"

class MultiwayTrie {
    public:
        Node* root;               // root node of Multiway Trie
        bool find(std::string word);   // "find" function of MultiwayTrie class
        void insert(std::string word); // "insert" function of MultiwayTrie class
        void remove(std::string word); // "remove" function of MultiwayTrie class
        MultiwayTrie();           // MultiwayTrie constructor
        ~MultiwayTrie();          // MultiwayTrie destructor
};
