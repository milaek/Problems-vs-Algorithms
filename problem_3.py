def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # edge case of an empty array
    if len(input_list) < 1:
        return []
    if len(input_list) == 1:
        return input_list[0], 0
    # // incoming array by 2. if %len != 0, we expect the len of nums to be uneven, one @ // and one at //-1 in len
    len_2 = (len(input_list))//2
    len_1 = len(input_list) - len_2
    len_1 = (10**len_1)/10
    len_2 = (10**len_2)/10

    # sort array into max heap
    for i in range(len(input_list)//2 - 1, -1, -1):
        heapify(input_list, len(input_list), i)

    # pull highest number back and forth for the two ints
    num_1 = 0
    num_2 = 0

    while len(input_list) > 1:
        num_1 += pop(input_list)*len_1
        len_1 /= 10
        num_2 += pop(input_list)*len_2
        len_2 /= 10

    if len(input_list) == 1:
        num_1 += pop(input_list)

    return num_1, num_2


def pop(arr):
    """
    A helper function to pop an item from the heap and rebalance
    :param arr: max heap sorted array
    :return: largest number
    """
    arr[0], arr[-1] = arr[-1], arr[0]
    num = arr.pop()
    heapify(arr, len(arr), 0)
    return num


def heapify(arr, n, i):
    """
    :param arr: incoming array
    :param n: size of heap
    :param i: parent location
    :return:
    """
    # helper function to sort the heap
    parent = i
    l_child = 2*i + 1
    r_child = 2*i + 2

    # See if left child of root exists and is bigger
    if l_child < n and arr[parent] < arr[l_child]:
        parent = l_child

    # See if right child of root exists and is bigger
    if r_child < n and arr[parent] < arr[r_child]:
        parent = r_child

    # check if root needs to change and do so
    if parent != i:
        arr[i], arr[parent] = arr[parent], arr[i]  # swap

        # Heapify the new root.
        heapify(arr, n, parent)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#    TESTS    #
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case_2 = [[1, 2, 3, 4, 5], [542, 31]]
test_case_3 = [[], []]
test_case_4 = [[1], [1, 0]]
test_function(test_case_1)
test_function(test_case_2)
test_function(test_case_3)
test_function(test_case_4)
