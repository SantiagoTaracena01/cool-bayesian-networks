def get_max(array):
    max_value = array[0]
    for element in array[1:]:
        if element > max_value:
            max_value = element
    return max_value
