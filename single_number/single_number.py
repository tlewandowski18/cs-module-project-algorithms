'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#Objective is to find the number that only appears once in the given list
#Questions I might ask:
  #Do I have the objective correct?
  #Can we assume the data is always good?

Naive Approach
def single_number(arr):
    # Your code here
    #create an empty dictionary to hold first pass count
    ints = {}
    #iterate through list using indexes
    for i in range(len(arr)):

        #check if index is in created dict
        if arr[i] in ints.keys():
        #if int at index not in created dict create entry with key set to int and value set to 1(representing count)
            ints[arr[i]] = 2
        #if int at index already a key in dict, increment value by one
        else:
            ints[arr[i]] = 1
    #return key where value is equal to one
    for int, count in ints.items():
        if count == 1:
            return int


        
    



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
