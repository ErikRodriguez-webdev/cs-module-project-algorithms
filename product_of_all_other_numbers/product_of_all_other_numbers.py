'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # Create new array with multiplied values
    new_list = []
    # make for loop (i)
    for i in range(len(arr)):
        # set copy_arr here
        copy_list = arr.copy()
        # copy_arr.pop(i) to remove current index / value
        copy_list.pop(i)
        # new total per index
        total_value = 1
        # make another for loop (j)
        for j in range(len(copy_list)):
            # loop through to add integers and place in new array with multiplied values (i)
            total_value = total_value * copy_list[j]
            # when finished add total_value to its corresponding index (i) on new_list
            if j == len(copy_list) - 1:
                new_list.insert(i, total_value)

    return new_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
