'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # set i = 0
    i = 0
    too_long = 0
    zero_counter = 0
    # set move_zero = True
    move_zero = True
    # make while loop run until move_zero is false (i)
    while move_zero:
        print(arr)
        # safety net for infinite loop
        # if i > 500, then break
        # too_long += 1

        # if too_long > 50:
        #     break

        # if i == length of array
        if i == len(arr):
            zeroes = [0] * zero_counter
            arr.extend(zeroes)
            print(arr)
            return arr

        # if arr[i] == 0
        if arr[i] == 0:
            # zero_counter += 1
            zero_counter += 1
            # arr.pop(i)
            arr.pop(i)
            # subtract 1 from i
            i -= 1

        # add 1 to i
        i += 1


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
