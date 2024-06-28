print("Hello World")
print(6)
print("Hey",8)
print(9*9)
print("hey \nRiya")
# for comment line
"""
k
j
""" # """ ye v comment k liye h 
print("Hey \"Riya\"")
print("Hey",6,7,sep="~", end="0007")
print("riya")

#Variables and Data Types
a=100
a1=20
b=True
c="Riya"
d=None
e=complex(9,7)
print(a+a1)
print(e)
print(a+e)

# list1=[8,2.3,[-4,5],["apple","banana"]]
# print(list1)
# tuple1(("parrot","sperrow"),("lion","tiger"))
# print(tuple1)
# dict1={"name":"Riya","age":20}
# print(dict1)

#Type Casting
# 1)Explicit 
x="4"
y="5"
print(int(x)+int(y))

String="79"
num=9
String_num=int(String)
sum=num+String_num
print(sum)

# 2)Implicit
p=1.88
q=78
print(p+q)

s=4
print(type(s))

#Strings
name="Riya"
apple='''oiii  oii 
oii oi oi 
oi 
oi oi oi '''
print("Hello "+name)
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#using for loop
print("Using for loop")
for character in name:
    print(character)