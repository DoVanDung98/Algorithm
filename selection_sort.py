def selection_sort(array):
    """create a selection_sort algorithm

    Args:
        array ([array]): input array need apply selection sort algorithm
    """
    for i in range(len(array)-1):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx]>array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


if __name__=='__main__':
    array = [1,34,5,6,12,4,87,9]
    print('Array before apply selection sort algorithm: ', array)
    selection_sort(array)
    print('Array applied selection sort algorithm: ', array)
