#include "list.h"
#include <iostream>
#include <format>

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

int main() {
  list::Lexicon lexicon;
  test(lexicon);
  return 0;
}