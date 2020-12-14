def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list
       number: Input array to search and the target
    Returns:
       int: Index or -1
    """
    # check center
    half = (len(input_list)-1)//2

    beginning = 0
    end = len(input_list) - 1

    while beginning <= end:
        center = input_list[half]
        # check for correct values on potential checkpoints
        if center == number:
            return half
        if input_list[beginning] == number:
            return beginning
        if input_list[end] == number:
            return end

        if number > center:
            # if bigger than center check beginning
            if number < input_list[beginning]:
                # if smaller than beginning recurse right half
                beginning = half+1
            else:
                # if bigger than beginning recurse left half
                end = half-1
        else:
            if number == input_list[end]:
                return end
            # if smaller than center check then end
            if number < input_list[end]:
                # if smaller than the end recurse right
                beginning = half+1
            else:
                # if bigger recurse left
                end = half-1
        # calculate for next loop
        half = (end-beginning)//2
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


#    TESTS    #
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])