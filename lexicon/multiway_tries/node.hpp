#pragma once

class Node {
    public:
        bool is_word;       // Node's "word" label
        Node* children[26]; // children[0] corresponds to 'A', children[1] to 'B', etc.
        Node();             // Node constructor
        ~Node();            // Node destructor
};