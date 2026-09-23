#calculating the factorial of a given number using function
def fact(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans
a=int(input("Enter the number and find the factorial of the given number:"))
ans2=fact(a)
print("The factorial of the number",a,"=",ans2)    
