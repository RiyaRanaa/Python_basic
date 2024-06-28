def reverse(n,rev):
    assert n>=0
    if n==0:
        return rev
    else:
        r=n%10
        rev=rev*10+r
        return reverse(n//10,rev)
def main():
    
    n=int(input("Enter digit: "))
    print(reverse(n,0))
main()