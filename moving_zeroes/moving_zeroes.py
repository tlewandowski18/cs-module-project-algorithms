'''
Input: a List of integers
Returns: a List of integers
'''
#Objective - move all zeros to right end of list and all non-zeroes to left end
def moving_zeroes(arr):
    #Your code here
    #create a new array
    new_arr = []
    #iterate through list:
    for i in range(len(arr)):
        #if item does equals zero add zero to end of list
        if arr[i] == 0: 
            new_arr.append(arr[i])
        #if item does not equal zero add item to beginning of list
        else:
            new_arr.insert(0, arr[i])
            
    return new_arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")