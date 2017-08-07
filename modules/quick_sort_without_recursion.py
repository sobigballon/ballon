"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    high=len(array)-1
    low=0
    if high==0:
        return array
    while high>low:
        while high>low and array[high]<=array[low]:
            temp=array[high]
            array[high]=array[low]
            array[low]=array[high-1]
            array[high-1]=temp
            high=high-1
        while high>low and array[high]>array[low]:
            low=low+1
    l=high-2
    r=low+1
    low=0
    high=len(array)-1
    while high>r:
        while high>r and array[high]<=array[r]:
            temp=array[high]
            array[high]=array[r]
            array[r]=array[high-1]
            array[high-1]=temp
            high=high-1
        while high>r and array[high]>array[r]:
            r=r+1
    while l>low:
        if l>low and array[l]<=array[low]:
            temp=array[l]
 #           print(array[low])
            array[l]=array[low]
            array[low]=array[l-1]
            array[l-1]=temp
            l=l-1
        else:
             low=low+1
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
