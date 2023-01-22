#pragma once

#include <list>
#include <string>

namespace list {
  class Lexicon {
    public:
      bool find(std::string word);
      void insert(std::string word);
      void remove(std::string word);
    private:
      std::list<std::string> linkedList;
  };
}