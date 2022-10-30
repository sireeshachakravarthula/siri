num=int(input("enter the number:"))
sum=num #temp veriable
b=len(str(num)) #to know the length of the number
sum1=0
while num!=0: # 153
    r=num%10 #153%10=3
    sum1=sum1+(r**b) #3**3=9
    num=num//10 #15
if sum==sum1:
    print("armstrong number")
else:
    print("Not a armstrong number")



