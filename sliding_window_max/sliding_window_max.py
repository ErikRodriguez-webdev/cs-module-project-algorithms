'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # set answer_list here
    answer_list = []
    # set temp_list
    temp_list = []

    # make for loop (i)
    for i in range(len(nums)):
        # append nums[i] to temp_list
        temp_list.append(nums[i])

        # check if len(temp_list) == k
        if len(temp_list) == k:
            # then find max value of temp_list and append to answer_list
            value = max(temp_list)
            answer_list.append(value)
            # pop 0 index
            temp_list.pop(0)

    return answer_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
