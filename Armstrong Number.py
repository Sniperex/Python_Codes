sum=0
num1=input("Enter Number: ")
for i in num1:
    sum=sum+int(i)**len(num1)
if sum==int(num1):
    print(num1,"is Armstrong Number")
else:
    print(num1,"is not an Armstrong Number")
    





