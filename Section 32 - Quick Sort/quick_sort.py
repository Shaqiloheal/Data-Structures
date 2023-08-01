def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

my_list = [82, 9, 55, 27, 41, 69, 38, 15, 91, 31, 98, 45, 21, 8, 64, 88, 53, 16, 74, 70,
11, 94, 50, 97, 63, 85, 89, 72, 56, 80, 37, 47, 40, 26, 86, 43, 28, 99, 58, 17,
77, 68, 10, 65, 90, 35, 79, 1, 76, 3, 29, 7, 48, 54, 51, 5, 92, 2, 46, 14, 93,
39, 100, 75, 57, 32, 13, 83, 84, 96, 60, 36, 30, 66, 4, 22, 87, 62, 95, 61, 6,
23, 59, 12, 44, 25, 19, 67, 49, 33, 78, 24, 73, 34, 71, 20, 18, 42, 81, 52
]

print(quick_sort(my_list))