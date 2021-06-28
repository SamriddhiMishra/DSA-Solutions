# I - height, max  O - NoOfways
# Time - O(max^height), Space - O(1)
def stair(h, m, c):
    if h == 0:
        c = c+1
    elif h < 0:
        return c
    else:
        for i in range(1, m+1):
            c = stair(h-i, m,c)
    return c
        
print(stair(4,2, 0))