def fibonacci(num):
    if num <=1 :
        return num
    else :
        return fibonacci(num-1)+fibonacci(num-2)

num = int(input("Enter number : "))
print("Fibonacci Sequence : ")
for i in range(num):
    print(fibonacci(i),end= " ")