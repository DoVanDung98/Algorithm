def buble_sort(array):
    """ buble_sort algorithm

    Args:
        array ([array]): input array need apply buble sort algorithm
    """
    for j in range(len(array)):
        for i in range(len(array)-1-j):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

if __name__=='__main__':
    array = [1,34,5,6,12,4,87,9]
    print('Array before apply buble sort algorithm: ', array)
    buble_sort(array)
    print('Array applied buble sort algorithm: ', array)