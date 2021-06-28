# I-string, O - reverse

def rev(s, n):
    if n == len(s):
        return ""
    return rev(s, n+1) + s[n] 

print(rev("abchwegjchv", 0))
    