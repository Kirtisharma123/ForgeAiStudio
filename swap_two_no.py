#SWAP TWO NUMBERS
#INPUT 2 NUMBERS,SWAP THEM

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("Value of a initially:",a)
print("Value of b initially:",b)

c=b
b=a
a=c

print("Value of a after swapping:",a)
print("Value of b after swapping:",b)