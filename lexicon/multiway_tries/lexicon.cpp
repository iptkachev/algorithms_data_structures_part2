#include "tree.hpp"

bool Lexicon::find(string word) {
    return mwt.find(word);
}

void Lexicon::insert(string word) {
    mwt.insert(word);
}

void Lexicon::remove(string word) {
    mwt.remove(word);
}