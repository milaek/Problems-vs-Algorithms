def sqrt(num):
    """
    Calculate the floored square root of a number

    Args:
       num(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # edge case for 1
    if num == 1:
        return num
    if num < 0:
        return None

    half = num//2
    while half*half != num:
        if half*half > num:
            half = half//2
        else:
            half += half//2
        if half*half < num < (half + 1)*(half + 1):
            return half
    return half


#    TESTS    #
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (None is sqrt(-1)) else "Fail")
print("Pass" if (13 == sqrt(177)) else "Fail")