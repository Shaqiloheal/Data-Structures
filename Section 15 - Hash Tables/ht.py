"""
HashTable is a data structure that offers fast insertion, deletion and retrieval 
operations. This implementation uses the chaining method for handling collisions. 
Collisions occur when multiple keys map to the same index. Chaining handles 
collisions by allowing each index to hold a reference to multiple items.
"""
class HashTable:

    """
    The HashTable constructor. Initializes an empty hash table with a specified size.
    If no size is provided, default size will be 7.
    """
    def __init__(self,size=7):
        # Initialize an empty list with size 'size', all elements set to None
        self.data_map = [None] * size

    """
    This is a private method to hash a key. 
    The function computes a unique index for a given key.
    """
    def __hash(self,key):
        # Initialize the hash value to 0
        my_hash = 0
        # Iterate over each character in the key
        for letter in key:
            # For each character, add its ASCII value multiplied by 23 to the hash value
            # The modulo operation ensures that the hash value fits within the data_map list
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        # Return the final computed hash value
        return my_hash

    """
    Prints the current state of the hash table. 
    Each index-value pair in the data_map list is printed.
    """
    def print_table(self):
        # Enumerate through data_map list, i gets index and val gets the value at that index
        for i, val in enumerate(self.data_map):
            # Print the index-value pair
            print(i, ": ", val)

    """
    Inserts a new key-value pair into the hash table.
    """
    def set_item(self,key,value):
        # Generate a hash value for the key
        index = self.__hash(key)
        # If the index in the data_map list is empty (None), initialize a new list at that index
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Append the key-value pair to the list at the computed index
        self.data_map[index].append([key,value])

    """
    Retrieves the value associated with a given key in the hash table. 
    """
    def get_item(self,key):
        # Generate a hash value for the key
        index = self.__hash(key)
        # If there are key-value pairs at the computed index in the data_map list
        if self.data_map[index] is not None:
            # Iterate over each key-value pair at the index
            for i in range(len(self.data_map[index])):
                # If the key of a pair matches the input key, return the associated value
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        # If the key was not found, return None
        return None

    """
    Returns a list of all keys in the hash table.
    """
    def keys(self):
        # Initialize an empty list to store the keys
        all_keys = []
        # Iterate over each index in the data_map list
        for i in range(len(self.data_map)):
            # If there are key-value pairs at the current index
            if self.data_map[i] is not None:
                # Iterate over each key-value pair at the index
                for j in range(len(self.data_map[i])):
                    # Append the key of the pair to the all_keys list
                    all_keys.append(self.data_map[i][j][0])
        # Return the list of all keys
        return all_keys
    

    def item_in_common(list1,list2):
        """
        Check if the two input lists have at least one item in common using a naive approach.

        This function works by iterating over each item in the first list, and for each item,
        iterating over the second list to see if the item is present. As soon as it finds a match,
        it returns True. If no common item is found after checking all items, it returns False.

        This naive approach has a time complexity of O(n^2), where n is the length of the lists. 
        This is because in the worst case it requires comparing each item of the first list with 
        each item of the second list.

        Parameters:
        list1 (List): The first list to be compared.
        list2 (List): The second list to be compared.

        Returns:
        bool: True if there is at least one common item between the two lists, False otherwise.
    """
        for i in list1:
            for j in list2:
                if i == j:
                    return True
        return False
    
    def item_in_common_efficent(list1,list2):
        """
        Check if the two input lists have at least one item in common using an efficient approach.

        This function first creates a dictionary with the elements of the first list as keys.
        Then, it iterates over the second list and checks if any element is present in the dictionary.

        This efficient approach has a time complexity of O(n), where n is the length of the lists. 
        This is because in the worst case it requires traversing each list once.

        Parameters:
        list1 (List): The first list to be compared.
        list2 (List): The second list to be compared.

        Returns:
        bool: True if there is at least one common item between the two lists, False otherwise.
        """

        # Initialize an empty dictionary
        my_dict = {}
        # Iterate over each item in the first list
        for i in list1:
            # For each item, add it to the dictionary as a key with value True
            my_dict[i] = True
        # Iterate over each item in the second list
        for j in list2:
            # If the item is found as a key in the dictionary, return True
            if j in my_dict:
                return True
        # If no common item is found after checking all items, return False
        return False

    

# Create an instance of the HashTable class
my_hash_table = HashTable()

# Set items in the hash table
my_hash_table.set_item('bolts',1400)  # Insert key 'bolts' with value 1400 into the hash table
my_hash_table.set_item('washers',50)  # Insert key 'washers' with value 50 into the hash table
my_hash_table.set_item('lumber',70)  # Insert key 'lumber' with value 70 into the hash table

# Print the current state of the hash table
my_hash_table.print_table()

print()

# Get and print the values associated with specific keys in the hash table
print(my_hash_table.get_item('bolts'))  # Get value associated with key 'bolts'
print(my_hash_table.get_item('bricks'))  # Get value associated with key 'bricks'
print(my_hash_table.get_item('lumber'))  # Get value associated with key 'lumber'

print()

# Get and print all keys currently in the hash table
print(my_hash_table.keys())


print()
# Invoke the 'item_in_common' method on the HashTable class, passing two lists: [1,3,5] and [2,4,7].
# This method checks if the two lists have any common items, and returns a Boolean value accordingly.
# The result of this operation is then printed to the console.
print(HashTable.item_in_common([1,3,5],[2,4,7])) # False
print(HashTable.item_in_common([1,3,5],[2,4,5])) # True

print()
print(HashTable.item_in_common_efficent([1,3,5],[2,4,7])) # False
print(HashTable.item_in_common_efficent([1,3,5],[2,4,5])) # True
