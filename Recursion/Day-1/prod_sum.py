# I - Special array , O - Product Sum
# Special array- !empty & [int, special]
# prod sum = depth * [array sum [depth * array sum]]
# [] depth - 1, [[]] - 2

def is_special(arr):
    if not len(arr):
        return False
    else:
        for i in arr:
            if not isinstance(i, int) and  not is_special(i):
                return False
    return True
            
# print(is_special([]))

def prod_sum(arr, d):
    if not is_special(arr):
        return "Array is not special!"
    s = 0
    for i in arr:
        if isinstance(i, int):
            s = s+i
        else:
            s = s+ prod_sum(i, d+1)
    return d*s

print(prod_sum([5,2,[7, -1],3,[6,[-13,8],4]], 1))