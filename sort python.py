'''
    几个排序算法的python实现
    冒泡排序 选择排序 插入排序 快速排序
    还有 希尔排序 归并排序 堆排序
    
    you_shoubian
'''

import random

# 冒泡排序
def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        flag = True
        for j in range(1,length-i):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                flag = False
        if flag:
            return arr

# 选择排序
def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        first = i
        for j in range(first+1,length):
            if arr[first] > arr[j]:
                arr[first],arr[j] = arr[j],arr[first]
    return arr

# 插入排序
def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            for j in range(i-1,-1,-1):
                if arr[j] < temp:
                    arr[j+1] = arr[j]
                else:
                    arr[j] = temp
                    break
    return arr

# 快速排序
def quickSort(arr):
    length = len(arr)
    little = []
    equal = []
    great = []
    if length <= 1:
        return arr
    else:
        base = arr[0]
        for i in range(length):
            if arr[i] < base:
                little.append(arr[i])
            elif arr[i] > base:
                great.append(arr[i])
            else:
                equal.append(arr[i])
        little = quickSort(little)
        great = quickSort(great)
        return little + equal + great            

# 《Python cookbook 第二版》传说中的三行实现python快速排序。
def qSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        return qSort([x for x in arr[1:] if x < arr[0]])+ [arr[0]] + qSort([x for x in arr[1:] if x >= arr[0]])

# 获取随机数
def getRandom(len,m=0,n=10):
    randomList = []
    for i in range(len):
        randomList.append(random.randint(m,n));
    return randomList
    
if __name__ == "__main__":
    nums = getRandom(10,-100,100)
    print(nums)
    print('bubbleSort>>>    ',bubbleSort(nums))
    print('selectionSort>>> ',selectionSort(nums))
    print('insertSort>>>    ',insertSort(nums))
    print('quickSort>>>     ',quickSort(nums))
    print('qSort>>>         ',qSort(nums))
    