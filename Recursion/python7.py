#finding the factorial of the given number using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    factorial=n*fact(n-1)
    return factorial
a=int(input("Enter the number and find the factorial of the given number:"))
ans=fact(a)
print("Factorial of the given number",ans)