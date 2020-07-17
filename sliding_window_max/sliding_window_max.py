'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    #create new_array
    new_array = []
    #iterate through given arr:
    for i in range(len(nums)):
        #create sub_array that contains values from given array starting at current index and running up to but not including current index + k
        sub_array = nums[i:i+k]
        #make sure sub_array has length of k
        if len(sub_array) == k:
            #if so append max of sub_array to new_array
            new_array.append(max(sub_array))
    return new_array

   


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
