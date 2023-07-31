def selection_sort(my_list):
    # Outer loop to traverse through the list from the beginning to the second-to-last element
    for i in range(len(my_list) - 1):
        # Assume the current index 'i' as the index of the minimum value
        min_index = i

        # Inner loop to find the index of the minimum value in the unsorted portion of the list
        for j in range(i+1, len(my_list)):
            # Compare the element at index 'j' with the element at the current minimum index 'min_index'
            # If the element at index 'j' is smaller, update 'min_index' to 'j'
            if my_list[j] < my_list[min_index]:
                min_index = j

        # After finding the minimum value in the unsorted portion,
        # swap it with the element at index 'i' (current position of the outer loop)
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    # Return the sorted list after all iterations are complete
    return my_list


my_list = [4,2,6,5,1,3]
print(my_list)
print(selection_sort(my_list))