#include <string>
#include "node.hpp"
#include "tree.hpp"

MultiwayTrie::MultiwayTrie(void) {
    root = new Node();            // initialize instance variable
}

MultiwayTrie::~MultiwayTrie(void) {
    delete root;                  // call the root node's destructor
}

bool MultiwayTrie::find(std::string word) {
    Node* currNode = root;
    for (auto ch: word) {
        if (currNode->children[ch - 'a'] == 0) {
            return false;
        }
        currNode = currNode->children[ch - 'a'];
    }

    return currNode->is_word;
}

void MultiwayTrie::insert(std::string word) {
    Node* currNode = root;
    for (auto ch: word) {
        if (currNode->children[ch - 'a'] == 0) {
            currNode->children[ch - 'a'] = new Node();
        }
        currNode = currNode->children[ch - 'a'];
    }
    currNode->is_word = true;
}

void MultiwayTrie::remove(std::string word) {
    Node* currNode = root;
    for (auto ch: word) {
        if (currNode->children[ch - 'a'] == 0) {
            return;
        }
        currNode = currNode->children[ch - 'a'];
    }
    currNode->is_word = false;
}
