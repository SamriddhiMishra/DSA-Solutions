# I - string , O - all permutations

def perm(s, f, n):
    if n == len(s):
        f.append(s.copy()) # if don't push the copy then address of all same, so get modified
    
    for i in range(n,len(s)):
        s[i], s[n] = s[n], s[i]
        perm(s, f, n+1)
        s[i], s[n] = s[n], s[i]
        
    return f

f = perm(list("abc"), [], 0)
for i in f:
    print("".join(i))
    