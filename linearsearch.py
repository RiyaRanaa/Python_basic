l=[6,9,5,4,8,2,3]
key=8
def lins(l,key):
    for i in range(len(l)):
        if key==l[i]:
            return f"{key} found at index {i}"
    return f"{key} not found"
print(lins(l,key))

