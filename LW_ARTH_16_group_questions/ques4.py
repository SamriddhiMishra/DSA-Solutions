def sort(a, b, c): 
    if a > b and c > b:
        if a> c:
            l = [a,c,b]
        else:
            l = [c,a,b]
    elif b > a and c > a:
        if b> c:
            l = [b,c,a]
        else:
            l = [c,b,a]
    else:
        if b> a:
            l = [b,a,c]
        else:
            l = [a,b,c]
    return l
            
def descend(a, b,c):
    a,b,c = sort(a, b, c)
    print("{} > {} > {}".format(a,b,c))
    
def ascend(a, b,c):
    l = sort(a, b, c)
    l.reverse()
    a,b,c = l
    print("{} < {} < {}".format(a,b,c))
            
ascend(0,2,1)
descend(0,2,1)
    