#calculating the sum of the elements in the list with the help of the function
def get_sum(list):
    sum=0
    for i in range(0,len(list),1):
        sum=sum+list[i]
    return sum
x=[35,45,67,89,90]
ans=get_sum(x)
print("The sum of the element in the given list=",ans)

    
