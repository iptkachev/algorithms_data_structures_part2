#pragma once
#include "tree.hpp"

class Lexicon {
    public:
        MultiwayTrie mwt;         // instance variable MultiwayTrie object
        bool find(string word);   // "find" function of Lexicon class
        void insert(string word); // "insert" function of Lexicon class
        void remove(string word); // "remove" function of Lexicon class
};
