# Function to merge two sorted lists into a single sorted list
def merge(list1, list2):
    combined = []  # Initialize an empty list to store the merged result
    i = 0  # Initialize a pointer 'i' for list1
    j = 0  # Initialize a pointer 'j' for list2

    # Compare elements from list1 and list2 and merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])  # Append the smaller element from list1 to the 'combined' list
            i += 1  # Move the pointer 'i' to the next element in list1
        else:
            combined.append(list2[j])  # Append the smaller element from list2 to the 'combined' list
            j += 1  # Move the pointer 'j' to the next element in list2

    # After the first while loop, one of the lists may still have some elements left.
    # Append the remaining elements from list1 (if any) to the 'combined' list
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # Append the remaining elements from list2 (if any) to the 'combined' list
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined  # Return the final merged list


# Function to perform merge sort on a list
def merge_sort(my_list):
    # Base case: if the list has only one element, it is already sorted
    if len(my_list) == 1:
        return my_list

    # Find the middle index of the list
    mid_index = int(len(my_list) / 2)

    # Recursively apply merge_sort on the left half of the list
    left = merge_sort(my_list[:mid_index])

    # Recursively apply merge_sort on the right half of the list
    right = merge_sort(my_list[mid_index:])

    # Merge the sorted left and right halves and return the final sorted list
    return merge(left, right)


original_list = [1,2,7,8,3,4,5,6]

print("Original List:", original_list)
print("\nSorted List:  ", merge_sort(original_list))