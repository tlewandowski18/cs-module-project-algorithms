'''
Input: a List of integers
Returns: a List of integers
'''
#Brute Force
# def product_of_all_other_numbers(arr):
#     # Your code here
#     #create new list
#     new_list = []
#     #iterate through the list:
#     for i in range(len(arr)):
#         #at each point create two sub-lists values on right and values on left
#         left_list = arr[:i]
#         right_list = arr[i+1:]
#         l_product = 1
#         r_product = 1
#         #iterate through the sublists, multiplying all values together
#         for num in left_list:
#             l_product *= num
#         for num in right_list:
#             r_product *= num
#         #multiply products from two sublists and append final product to new lists
#         new_list.append(l_product * r_product)
#     return new_list

def product_of_all_other_numbers(arr):
    new_array = []
    iterator
    for i in range (len(arr)):

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
