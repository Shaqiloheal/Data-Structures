def insertion_sort(my_list):
    # Start iterating from the second element (index 1) to the end of the list
    for i in range(1, len(my_list)):
        # Store the current element in a temporary variable 'temp'
        temp = my_list[i]

        # Initialize a variable 'j' to the index before the current element
        j = i - 1

        # While the element at 'j' is greater than 'temp' and 'j' is within the valid index range (not negative)
        # We move the elements greater than 'temp' one position ahead to create space for 'temp' in its correct position
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]  # Move the element at 'j' to the next position
            my_list[j] = temp  # Place 'temp' in the current position (j)

            # Decrement 'j' to continue checking and shifting elements in the sorted part of the list
            j -= 1

    # Return the sorted list after all iterations are complete
    return my_list


my_list = [4,2,6,5,1,3]
print(my_list)
print(insertion_sort(my_list))
        