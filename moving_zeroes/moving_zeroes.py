'''
Input: a List of integers
Returns: a List of integers
'''
#Objective - move all zeros to right end of list and all non-zeroes to left end
class Node:
    def __init__(self, value=None, next_node=None):
        self.value= value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None #stores a node that corresponds to our first node in list
        self.tail = None # stores a node that is the end of the list

    def add_to_head(self, value):
        #create a node to add
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        #create a node to add
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    
    
# def moving_zeroes(arr):
#     #Your code here
#     #create a new array
#     new_arr = []
#     #iterate through list:
#     for i in range(len(arr)):
#         #if item does equals zero add zero to end of list
#         if arr[i] == 0: 
#             new_arr.append(arr[i])
#         #if item does not equal zero add item to beginning of list
#         else:
#             new_arr.insert(0, arr[i])
            
#     return new_arr

def moving_zeroes(arr):
    new_list = LinkedList()
    for i in range(len(arr)):
        if arr[i] == 0:
            new_list.add_to_tail(arr[i])
        else:
            new_list.add_to_head(arr[i])
    iterator = new_list.head
    final_list = []
    while iterator is not None:
        final_list.append(iterator.value)
        iterator = iterator.next_node
    return final_list



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")