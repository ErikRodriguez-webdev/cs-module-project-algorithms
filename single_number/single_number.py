'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# XOR operator look it up later


def single_number(arr):
    # Your code here
    # for loop through list
    for i in range(len(arr)):
        # use method to count the number of times a value pops up in list
        # if it equals one then return the value that is not a duplicate
        if arr.count(arr[i]) == 1:
            return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
