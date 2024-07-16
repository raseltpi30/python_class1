result = 0
for num in range(1,101):
    if num % 5 == 0:
        print(num)
        result+=num
print("sum is :", result)

result = 0
for num in range(1,1001):
    if num % 100==0:
        print(num)
        result+=num 
print("The sum is :",result)

result = 0
for i in range(1,10):
    if i % 2 != 0 and i % i == 0:
        print(i)