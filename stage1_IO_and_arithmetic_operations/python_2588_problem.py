x=int(input())
y=int(input())
f1=(y%10)*x
f2=(((y%100)//10)*x)
f3=(y//100)*x
f4=(f1+f2*10+f3*100)
print(f1)
print(f2)
print(f3)
print(f4)

##second way


#num1 = int(input()) 
#num2 = input() 
#for num in list(num2[::-1]): 
#	print(num1 * int(num)) 
#print(num1 * int(num2))
