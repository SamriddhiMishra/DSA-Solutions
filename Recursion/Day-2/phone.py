# I - phoneno , O - patterns
# Time - O(4*NoOfDigits), Space - O(n*(3^n))
def mnemo(p, s, n):
    if n == len(p):
        f.append(s)
        return
    d = p[n]
    if d == '0':
        mnemo(p, s+'0', n+1)
    elif d == '1':
        mnemo(p, s+'1', n+1)
    elif d == '2':
        mnemo(p, s+'a', n+1)
        mnemo(p, s+'b', n+1)
        mnemo(p, s+'c', n+1)
    elif d == '3':
        mnemo(p, s+'d', n+1)
        mnemo(p, s+'e', n+1)
        mnemo(p, s+'f', n+1)
    elif d == '4':
        mnemo(p, s+'g', n+1)
        mnemo(p, s+'h', n+1)
        mnemo(p, s+'i', n+1)
    elif d == '5':
        mnemo(p, s+'j', n+1)
        mnemo(p, s+'k', n+1)
        mnemo(p, s+'l', n+1)
    elif d == '6':
        mnemo(p, s+'m', n+1)
        mnemo(p, s+'n', n+1)
        mnemo(p, s+'o', n+1)
    elif d == '7':
        mnemo(p, s+'p', n+1)
        mnemo(p, s+'q', n+1)
        mnemo(p, s+'r', n+1)
        mnemo(p, s+'s', n+1)
    elif d == '8':
        mnemo(p, s+'t', n+1)
        mnemo(p, s+'u', n+1)
        mnemo(p, s+'v', n+1)
    elif d == '9':
        mnemo(p, s+'w', n+1)
        mnemo(p, s+'x', n+1)
        mnemo(p, s+'y', n+1)
        mnemo(p, s+'z', n+1)
f = []
mnemo('1905', '', 0)
print(f)
        
        
        
    