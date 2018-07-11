
def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p+1, hi)
    return lst

def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            print(lst)
    if lst[hi-1] < lst[i+1]:
        lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
        print(lst)
    return i+1


print(quicksort([2, 3, 1, 5, 7, 8, 4], 0, 7))