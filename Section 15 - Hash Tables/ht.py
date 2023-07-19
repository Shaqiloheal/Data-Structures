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
