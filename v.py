# 23. Write a program to print all numbers between 1 and 50 that are divisible by both 3 and 5.
a=[]
for i in range(1,51):
    if(i%3==0 and i%5==0):
        a.append(i)

print(a)