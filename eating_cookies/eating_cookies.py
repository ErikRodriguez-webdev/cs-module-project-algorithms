'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # check if n == 0 to see if cookie eating plan is valid
    if n == 0:
        # then return 1
        return 1

    # check if n < 0 to return an integer that will not increase our cookie eating plan
    if n < 0:
        # then return 0
        return 0

    # else
    else:
        # then return eating_cookie(n-1), eating_cookie(n-2), eating_cookie(n-3)
        return eating_cookies((n-1)) + eating_cookies((n-2)) + eating_cookies((n-3))


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
