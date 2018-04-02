def array_chunk(array, size):
    """
    Given an array and chunk size, divide the array
    into many subarrays, where each subarray is of
    length size.
    array_chunk([1,2,3,4], 2) --> [[1,2], [3,4]]
    array_chunk([1,2,3,4,5], 2) --> [[1,2], [3,4], [5]]
    """
    counter = 0
    outer_list = []
    inner_list = []

    for item in array:
        if counter > 0 and not counter % size:
            outer_list.append(inner_list)
            inner_list = [item]
        else:
            inner_list.append(item)

        counter += 1
    
    outer_list.append(inner_list)
    
    return outer_list

def array_chunk_slice(array, size):
    outer_list = []
    index = 0
    while index < len(array):
        outer_list.append(array[index:index+size])
        index += size
    return outer_list

