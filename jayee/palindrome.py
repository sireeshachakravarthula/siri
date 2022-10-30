#n=input("enter the value:")
#reverse =n[::-1]
#if(n == reverse):
    #print("yes it is palindrome")
#else:
 #   print("no it is not a palindrome")


n=int(input("enter the value:"))
temp=n
rev=0
while temp>0:
    r=temp%10
    rev=rev*10+r
    temp=temp//10
print("reverse of given number is",rev)
if rev==n:
    print(n,"is a palindrome")
else:
    print(n,"is not a palidrome")