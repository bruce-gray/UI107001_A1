def merge_sort(lst):
    # base case - list of 1 or 0 elements doesn't need to be sorted
    if len(lst) <= 1:
        return lst
    
    # split the list in half
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # merge the sorted halves
    return merge(left,right)

def merge(left,right): # compares the first unsorted values of left[] vs right[] and appends result[] with the lower value
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # append any remaining elements from either half
    result += left[i:]
    result += right[j:]
    return result