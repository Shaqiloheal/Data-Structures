def bubble_sort(my_list):
    # Outer loop to traverse through the list from the end to the beginning
    for i in range(len(my_list) - 1, 0, -1):
        # Inner loop to compare adjacent elements and perform swaps
        for j in range(i):
            # If the current element is greater than the next element, perform a swap
            if my_list[j] > my_list[j+1]:
                # Temporary variable 'temp' to hold the value of the current element temporarily
                temp = my_list[j]
                # Swap the current element with the next element
                my_list[j] = my_list[j+1]
                # Assign the value in 'temp' (original value of current element) to the next element
                my_list[j+1] = temp
    # Return the sorted list after all iterations are complete
    return my_list


print(bubble_sort([4,2,6,5,1,3]))