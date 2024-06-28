def reverse(str):
    if str=='':
        return str
    else:
        return str[-1]+reverse(str[:-1])
print(reverse("Riya Raj"))                                                     