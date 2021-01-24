
def find_length_circles(permutation):
    circles = []
    visited = [False for _ in range(len(permutation))]
    for i, start_sigma in enumerate(permutation):
        if i + 1 == start_sigma and not visited[i]:
            circles.append([start_sigma])
            visited[i] = True
        elif not visited[i]:
            cur_circle = []
            cur_circle.append(i + 1)
            cur_circle.append(start_sigma)
            visited[i] = True
            next_sigma = permutation[i]
            while permutation[next_sigma - 1] != i + 1:
                visited[next_sigma - 1] = True
                next_sigma = permutation[next_sigma - 1]
                cur_circle.append(next_sigma)
            visited[next_sigma - 1] = True
            circles.append(cur_circle)
    sum_length = 0
    for circle in circles:
        sum_length += len(circle) - 1
    return sum_length


if __name__ == '__main__':
    print(find_length_circles([1,4,2,5,6,3]))
    print(find_length_circles([2,1,4,3]))

