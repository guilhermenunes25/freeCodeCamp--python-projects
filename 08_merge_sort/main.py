def merge_sort(array):
    middle_point = array // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    merge_sort(left_part)