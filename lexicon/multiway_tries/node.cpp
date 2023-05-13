#include "node.hpp"

Node::Node(void) {          // initialize instance variables
    is_word = false;
    for(int i = 0; i < 26; ++i) {
        children[i] = 0;
    }
}

Node::~Node(void) {
    for(int i = 0; i < 26; ++i) {
        delete children[i]; // call my child nodes' destructors before deleting me
    }
} // now that all of my descendants have been destroyed, delete me
