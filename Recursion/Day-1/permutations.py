# I - array(unique integers) , O - permutations
# if empty array return empty


def perm(arr):
    if not len(arr):
        return [[]]
    l = []
    for i in range(len(arr)):
        d = arr.copy()
        f = d.pop(i)
        d = perm(d)
        for j in d:
            j.insert(0,f)
            l.append(j)
    return l
    


def permute1(a, l, r):
    if l==r:
        print (a)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute1(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
            
def permute2(arr):
    from itertools import permutations
    l = list(permutations(arr))
    print (l)

print(permute2([1,2,3]))

    