"""
bubble sort
heap sort
quick sort
insertion sort
selection sort
"""

lst = [1, 2, 5, 6, 11, 100, 55, 88, 99, 67]


def bubble_sort(numbers):
    for solda_kalanlar in range(len(numbers) - 1, 0, -1):
        for index in range(solda_kalanlar):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
    return numbers

def siftdown(lst, start, end):
    largest = end
    l = 2 * end + 1
    r = 2 * end + 2
    if l < start and lst[largest] < lst[l]:
        largest = l
    if r < start and lst[largest] < lst[r]:
        largest = r
    if largest != end:
        lst[end], lst[largest] = lst[largest], lst[end]
        siftdown(lst, start, largest)

def heap_sort(lst):
    for i in range(len(lst)//2 - 1, -1, -1):
        siftdown(lst, len(lst), i)
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        siftdown(lst, i, 0)
    return lst

def insertion_sort(lst):
    i = 0
    j = 0
    for index in range(len(lst)):
        j = index
        while(j > 0) and (lst[j - 1] > lst[j]):
            lst[j-1], lst[j] = lst[j], lst[j-1]
            j -= 1
    return lst

def selection_sort(lst):
    for i in range(len(lst)):
        min_id = i
        for j in range(i + 1, len(lst)):
            if lst[min_id] > lst[j]:
                min_id = j
        lst[i], lst[min_id] = lst[min_id], lst[i]
    return lst

def partition(lst, low, high):
    i = (low - 1)
    pivot = lst[high]

    for j in range(low, high):
        if lst[j] < pivot:
            i = i+1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1

def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi-1)
        quick_sort(lst, pi+1, high)
    return lst


print(quick_sort(lst, 0, len(lst) - 1))
