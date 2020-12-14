import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # edge case of empty ints
    if len(ints) < 1:
        return None, None
    # set initial values for min and max
    min_int = ints[0]
    max_int = ints[0]
    # run through ints once keeping track of min and max nums encountered
    for num in ints:
        if num < min_int:
            min_int = num
        if num > max_int:
            max_int = num
    return min_int, max_int


#    TESTS    #

# test 1 (pos ints)
lst = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(lst)
print("Pass" if ((0, 9) == get_min_max(lst)) else "Fail")

# test 2 (negative ints)
lst = [i for i in range(-30, 1)]
random.shuffle(lst)
print("Pass" if ((-30, 0) == get_min_max(lst)) else "Fail")

# test 3 (duplicate ints
lst = [i for i in range(0, 10)] + [i for i in range(0, 10)]
random.shuffle(lst)
print("Pass" if ((0, 9) == get_min_max(lst)) else "Fail")

# test 4 (empty list)
print("Pass" if (None, None) == get_min_max([]) else "Fail")

# test 5 (one item long list)
print("Pass" if (1, 1) == get_min_max([1]) else "Fail")

print("/".split("/"))


