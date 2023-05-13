#include "list.h"
#include <iostream>
#include <format>
#include <vector>
#include <string>

void test(list::Lexicon lexicon) {
  lexicon.insert("10");
  lexicon.insert("20");
  lexicon.remove("10");
  if (!lexicon.find("20")) {
    std::cout << "FAIL find 20\n";
  }
  if (lexicon.find("10")) {
    std::cout << "FAIL find 10\n";
  }
  if (lexicon.find("30")) {
    std::cout << "FAIL find 30\n";
  }  
}

void insert(std::vector<std::string>& array, std::string word) {
    std::vector<std::string>::iterator it = array.begin();
    std::vector<std::string>::iterator end = array.end();
    bool isInsert = false;
    while (it != end) {
    // std::cout << *it << "\n";
        if (*it >= word && not isInsert) {
            array.insert(it, word);
            isInsert = true;
            break;
        }
        ++it;
    }
    if (not isInsert) {
        array.push_back(word);
    }
}

void insert2(std::vector<std::string>& array, std::string word) {
    std::vector<std::string>::iterator low;
    low = std::lower_bound(array.begin(), array.end(), word);
    if (low == array.end()) {
        array.push_back(word);
    } else {
        array.insert(low, word);
    }
}

void remove(std::vector<std::string>& array, std::string word) {
    /* YOUR CODE HERE */
    std::vector<std::string>::iterator a;
    a = std::lower_bound(array.begin(), array.end(), word);
    array.erase(a); 
}

int main() {
  list::Lexicon lexicon;
  test(lexicon);
  std::vector<std::string> a;
  for (int i=0; i < 10; ++i) a.push_back(std::to_string(i));
  insert2(a, "-1");
  insert2(a, "11");
  insert2(a, "99");
  remove(a, "-1");
  for (auto o: a) std::cout << o << "\n";
  return 0;
}