def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # marks where the beginning of the unsorted list is
    beginning = 0
    # moves through list in order to sort
    mover = 0
    # marks where the end of the unsorted list is
    end = len(input_list) - 1

    while mover <= end:
        if input_list[mover] == 0:
            input_list[mover] = input_list[beginning]
            input_list[beginning] = 0
            beginning += 1
            mover += 1
        elif input_list[mover] == 2:
            input_list[mover] = input_list[end]
            input_list[end] = 2
            end -= 1
        else:
            mover += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


#    TESTS    #
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0, 0, 0])
test_function([])
