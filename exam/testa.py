from itertools import permutations


def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        all_p = list(all_perms(str[1:]))
        for perm in all_p:
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                print(perm[:i] + str[0:1] + perm[i:])
                yield perm[:i] + str[0:1] + perm[i:]


print(list(all_perms([1, 2, 4])))