#Without assert
salary=int(input("Enter salary:"))
if salary<100:
    print("POOR")
else:
    print("RICH")

#with assert
salary1=int(input("Enter salary:"))
assert salary>=0
if salary<100:
    print("POOR")
else:
    print("RICH")


