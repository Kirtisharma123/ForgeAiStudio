#SIMPLE CALCULATOR

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("First number is:",num1)
print("Second number is:",num2)

print("Select operations to perform:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter your choice between (1-4): "))
operations = {
    1:num1+num2,
    2:num1-num2,
    3:num1*num2,
    4:num1/num2

}

results=operations.get(choice,"Invalid Choice!")
print("Result",results)
