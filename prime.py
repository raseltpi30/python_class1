result = 0
for num in range(1,10):
# If given number is greater than 1
  if num > 1:    
    for i in range(2,(num//2)+1):
      if (num % i) == 0:
        break
    else:
      print(num)
      result+=num
print(result)

a = 10
for b in range(2,(a//2)+1):