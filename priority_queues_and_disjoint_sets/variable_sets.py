from priority_queues_and_disjoint_sets.merging_documents import Tables


class SystemVariables(Tables):
    def build_and_check_variables(self, equal_queries, non_equal_queries) -> int:
        is_right_system = 1
        for query in equal_queries:
            self.union(*query)

        for query in non_equal_queries:
            if self.is_one_set(*query):
                is_right_system = 0
                break
        return is_right_system

    def is_one_set(self, a: int, b: int) -> bool:
        root_a = self.fast_find(a)
        root_b = self.fast_find(b)
        return root_a == root_b

    def fast_find(self, i: int) -> int:
        while i != self.parents[i]:
            i = self.parents[i]
        return i


if __name__ == '__main__':
    n_variables = 6
    equal_queries = [(1, 2), (2, 4), (2, 3)]
    non_equal_queries = [(5, 4), (1, 3)]

    variables = SystemVariables([0 for _ in range(n_variables)])

    assert variables.build_and_check_variables(equal_queries, non_equal_queries) == 0
