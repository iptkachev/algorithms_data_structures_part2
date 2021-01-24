def colatc(num):
    len_seq = 0
    while True:
        if num % 2 == 0:
            num = num / 2
            len_seq += 1
            if num == 1:
                break
        else:
            num = 3 * num + 1
            len_seq += 1
    return len_seq


if __name__ =='__main__':
    assert colatc(17) == 12
    assert colatc(3) == 7
    assert colatc(5) == 5
    # start, end = 2, 5
    # start, end = map(int, input().split())
    # print(sum((colatc(i) for i in range(start, end + 1))))
