
def bsearch(l, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if x==l[mid]:
            return mid
        elif x<l[mid]:
            return bsearch(l, low, mid - 1, x)
        else:
            return bsearch(l, mid + 1, high, x)
    else:
        return -1
l=[9,4,8,2,6,7]
l.sort()
x = 8
result = bsearch(l, 0, len(l)-1, x)
if result!=-1:
    print(f"{x} is present at index {str(result)}")
else:
    print(f"{x} is not present in the list")

