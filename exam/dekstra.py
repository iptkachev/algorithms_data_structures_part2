

def deikstra_algo(contingency_dict, n_vertexes, start, finish):
    labeled_edges = [False for _ in range(len(contingency_dict))]
    paths_to_node = {i: None for i in range(len(contingency_dict))}
    min_cost_path_to_node = {i: float('inf') for i in range(len(contingency_dict))}

    next_nodes = [start]
    min_cost_path_to_node[start] = 0
    for i in range(n_vertexes):
        for node in next_nodes:
            if not labeled_edges[node]:
                neighbors = contingency_dict[node].keys()
                for neighbor in neighbors:
                    if not labeled_edges[neighbor]:
                        new_path = min_cost_path_to_node[node] + contingency_dict[node][neighbor]
                        if min_cost_path_to_node[neighbor] > new_path:
                            min_cost_path_to_node[neighbor] = new_path
                            paths_to_node[neighbor] = node
                labeled_edges[node] = True
                next_nodes = neighbors
    if min_cost_path_to_node[finish] == float('inf'):
        return -1
    return min_cost_path_to_node[finish]


def make_contingency_dict(n_vertexes, pair_vertexes):
    contingency_dict = {i: {} for i in range(n_vertexes)}
    for pair in pair_vertexes:
        contingency_dict[pair[0] - 1][pair[1] - 1] = 1
        contingency_dict[pair[1] - 1][pair[0] - 1] = 1
    return contingency_dict


if __name__ == '__main__':
    # contingency_dict = {
    #     0: {
    #         1: 1,
    #         3: 1
    #     },
    #     1: {
    #         0: 1,
    #         2: 1
    #     },
    #     2: {
    #         1: 1,
    #         3: 1,
    #         4: 1,
    #     },
    #     3: {
    #         2: 1,
    #         0: 1,
    #         4: 1
    #     },
    #     4: {
    #         3: 1,
    #         2: 1
    #     },
    #     5: {
    #         6: 1
    #     },
    #     6: {
    #         5: 1
    #     }
    # }
    # start = 0
    # print(deikstra_algo(contingency_dict, 6, start, 5))
    # print(deikstra_algo(contingency_dict, 6, start, 4))
    # print(deikstra_algo(contingency_dict, 6, start, 2))
    # print(deikstra_algo(contingency_dict, 6, start, 1))
    # print(deikstra_algo(contingency_dict, 6, 5, 6))

    # n_vertexes, _ = 4, 5
    # pair_vertexes = [(3,2),(4,2),(1,2),(1,4),(3,1)]
    # n_tests = 4
    # test_paths = [(3,1),(1,1),(1,3),(3,2)]

    _, n_vertexes = map(int, input().split())
    pair_vertexes = []
    for _ in range(n_vertexes):
        pair_vertexes.append(tuple(map(int, input().split())))

    n_tests = int(input())
    test_paths = []
    for _ in range(n_tests):
        test_paths.append(tuple(map(int, input().split())))

    contingency_dict = make_contingency_dict(n_vertexes, pair_vertexes)

    for start, finish in test_paths:
        print(deikstra_algo(contingency_dict, n_vertexes, start - 1, finish - 1))

