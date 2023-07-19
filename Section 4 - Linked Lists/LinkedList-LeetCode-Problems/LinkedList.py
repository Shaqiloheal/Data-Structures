class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value) # Create new node
        self.head = new_node   # Assign head pointer
        self.tail = new_node   # Assign tail pointer
        self.length = 1        # initalize length of LL

    def print_list(self):
        temp = self.head         # Assign pointer to head node
        while temp is not None:  # iterate through LL until end of LL
            print(temp.value)   # prints current node value
            temp = temp.next     # after printing node move to next node

    def append(self,value):
        new_node = Node(value)   # Create a new node
        if self.head is None:    # Check that head pointer is None
            self.head = new_node # Assign head pointer to new node
            self.tail = new_node # Assign tail pointer to new node
        else:
            self.tail.next = new_node   # Assign current tail pointer to new node
            self.tail = new_node        # tail pointer is now on the new node
        self.length += 1            # incremement LL length by 1.
        return True

    def pop(self):
        if self.length == 0:    # Check if LL is empty
            return None         # Do nothing if empty
        temp = self.head        # Store the reference to the current head
        pre = self.head         # Store the reference to the previous node
        while(temp.next):       # Traverse until the last node is reached
            pre = temp          # Update the previous node to the current node
            temp = temp.next    # Move to the next node
        self.tail = pre         # Update the tail to the previous node
        self.tail.next = None   # Set the pointer of the new tail to None
        self.length -= 1        # Decrease the length of the LL
        if self.length == 0:    # Check if the LL became empty after removing the last node
            self.head = None    # Set the head to None
            self.tail = None    # Set the tail to None
        return temp       # Return the removed node
    
    def prepend(self,value):
        new_node = Node(value)          # Create a new node
        if self.length == 0:            # Check if LL is empty
            self.head = new_node        # Assign head pointer to new node
            self.tail = new_node        # Assign tail pointer to new node
        else:
            new_node.next = self.head   # Set new node to point at head
            self.head = new_node        # Assign the head pointer to the new node
        self.length += 1                # incrememnt LL length by 1
        return True
    
    def pop_first(self):
        if self.length == 0:            # Check if LL is empty
            return None                 # Return None if LL is empty.
        temp = self.head                # Assign register to head node
        self.head = self.head.next      # Make the next node in the LL the new head node
        temp.next = None                # Disconnect the previous node from the LL
        self.length -= 1                # Decrement the LL length by one
        if self.length == 0:            # Check if the LL is now empty after popping the node
            self.tail = None            # If it is, also set the tail to None, there is no nodes left
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:  # check index is within LL limits
            return None                        # Return None if outwith limit
        temp = self.head                       # Assign register to head node
        for _ in range(index):                 # Iterate through the LL
            temp = temp.next                   # Move temp register to next node
        return temp                            # Return node when index is found
        
    def set_value(self,index,value):
        temp = self.get(index)        # Use get() to retrieve the node at the provided index and set temp to that node
        if temp:                      # Check if the node at the given index exists (if temp is not None)
            temp.value = value        # If it exists, set the node's value to the provided value
            return True               # Return True to indicate the operation was successful
        return False                  # If the node does not exist (temp is None), return False to indicate the operation failed
    
    def insert(self,index,value):
        if index < 0 or index > self.length: # Check if the index is within the valid range (0 to length of list)
            return False                     # If not within the valid range, return False as the operation is not possible
        if index == 0:                       # If index is 0, new node should be the head of list
            return self.prepend(value)       # Call prepend function to add the node at the beginning of the list
        if index == self.length:             # If index is equal to the length of list, new node should be the tail
            return self.append(value)        # Call append function to add the node at the end of the list
        new_node = Node(value)               # Create a new node with the given value
        temp = self.get(index - 1)           # Get the node currently at the position index - 1
        new_node.next = temp.next            # Assign the next node of the new node to be the next node of the temp node
        temp.next = new_node                 # Make the new node be the next node of the temp node
        self.length += 1                     # Increase the length of the list by 1 as a node is added
        return True
        
    def remove(self,index):
        if index < 0 or index >= self.length:  # Check if the index is within the valid range (0 to length of list - 1)
            return None                        # If not within the valid range, return None as the operation is not possible
        if index == 0:                         # If index is 0, the head of the list should be removed
            return self.pop_first()            # Call pop_first function to remove the node at the beginning of the list
        if index == self.length - 1:           # If index is equal to the length of list - 1, the tail should be removed
            return self.pop()                  # Call pop function to remove the node at the end of the list
        pre = self.get(index - 1)              # Get the node currently at the position index - 1
        temp = pre.next                        # The node to be removed is the next node of the previous node
        pre.next = temp.next                   # Adjust the next pointer of the previous node to skip over the node to be removed
        temp.next = None                       # Disconnect the node to be removed from the list by setting its next to None
        self.length -= 1                       # Decrease the length of the list by 1 as a node is removed
        return temp                            # Return the node that was removed
    
    def reverse(self):
        temp = self.head              # Save the head node in a temp variable
        self.head = self.tail         # Make the tail node the new head node
        self.tail = temp              # Make the former head node (saved in temp) the new tail node
        after = temp.next             # Save the next node of temp (former head node and new tail node) in after
        before  = None                # Initialize before variable as None, this will be the previous node as we traverse the list
        for _ in range(self.length):  # Loop over the linked list
            after = temp.next         # Save the next node of temp in after before changing temp.next
            temp.next = before        # Make the previous node (before) the next node of temp, effectively reversing the link
            before = temp             # Move the before pointer one step forward (i.e., make the current node the new before)
            temp = after              # Move the temp pointer one step forward (i.e., make the next node the new temp)
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print( my_linked_list.find_middle_node().value )


'''
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.reverse()



print("\nLinkedList key information:")
print("Head:",my_linked_list.head.value)
print("Tail:",my_linked_list.tail.value)
print("LinkedList Length:",my_linked_list.length)

print("\nmy_linked_list: ")
my_linked_list.print_list()
'''




