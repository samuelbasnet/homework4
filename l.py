# 8. Write a program to print the factorial of a number accepted from user.

a=int(input("Enter a number:"))
fact=1
for i in range(1,a+1):
    fact*=i
print("Factorial is:",fact)