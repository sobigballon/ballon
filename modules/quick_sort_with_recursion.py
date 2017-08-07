#!/usr/bin/python
# -*- coding: utf-8 -*-

def quick_sort_standord(array,low,high):
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low

if __name__ == '__main__':
    array2 = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]

    print array2
    quick_sort_standord(array2,0,len(array2)-1)
    print array2
