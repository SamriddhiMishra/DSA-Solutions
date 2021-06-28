# I - Array , O - Power Set(Including Empty)
# Time- O(n*n) Space - O(n *2^n)
def power_set(arr, n):
    if n >= len(arr):
        return [[]]
    f = arr[n]
    p = power_set(arr, n+1)
    for i in range(len(p)):
        if len(p[i]) == 0:
            p.append([f])
        else:
            e = p[i].copy() # don't put like p[i].copy().insert(0,f) gives None
            e.insert(0,f)
            p.append(e)
    return p

print(power_set([1,2,3], 0))
