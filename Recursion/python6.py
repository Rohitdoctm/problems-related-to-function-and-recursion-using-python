#finding the sum of first n natural numbers using recursion
def calc_sum(n):
    if(n==1):
        return 1
    sum=n+calc_sum(n-1)
    return sum
a=int(input("Enter the number"))
ans=calc_sum(a)
print("sum of the given number",ans)