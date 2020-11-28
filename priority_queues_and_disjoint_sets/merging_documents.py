from typing import List


class Tables:
    def __init__(self, rows: List[int]):
        self.rows = rows
        self.parents = list(range(len(rows)))
        self.ranks = [0 for _ in range(len(rows))]
        self.current_max = max(self.rows)

    def execute_query(self, destination: int, source: int) -> int:
        self.union(destination, source)
        return self.current_max

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.ranks[root_a] > self.ranks[root_b]:
            self.rows[root_b] += self.rows[root_a]
            self.rows[root_a] = 0
            self.parents[root_a] = root_b
        else:
            self.rows[root_a] += self.rows[root_b]
            self.rows[root_b] = 0
            self.parents[root_b] = root_a

            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_a] += 1

        self.current_max = max(self.current_max, self.rows[root_a], self.rows[root_b])

    def find(self, i: int) -> int:
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


if __name__ == '__main__':
    rows = [1, 1, 1, 1, 1]
    queries = [
        (3, 5), (2, 4), (1, 4), (5, 4), (5, 3)
    ]

    tables = Tables(rows)
    results = []
    for query in queries:
        res = tables.execute_query(query[0] - 1, query[1] - 1)
        results.append(res)

    assert results == [2, 2, 3, 5, 5]
