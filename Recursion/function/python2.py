#swapping the two numbers with the help of the third variable using function
def swap(a,b):
    temp=a
    a=b
    b=temp
    print("The number after swapping a=",a,"b=",b)
a=int(input("Enter the first number:"))
b=int(input("Enter the second  number:"))
print("The number before swapping a=",a,"b=",b)
swap(a,b)
