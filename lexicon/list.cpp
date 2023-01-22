#include <list>
#include <algorithm>
#include "list.h"

bool list::Lexicon::find(std::string word) {
  std::list<std::string>::iterator pointer;
  pointer = std::find(linkedList.begin(), linkedList.end(), word);
  if (pointer != linkedList.end()) {
    return true;
  }
  return false;
}

void list::Lexicon::insert(std::string word) {
  linkedList.push_back(word);
}

void list::Lexicon::remove(std::string word) {
  linkedList.remove(word);
}