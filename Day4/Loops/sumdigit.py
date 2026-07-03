num = int(input())

sum = 0
while num > 0:
    sum += num % 10
    num //= 10

print('Sum is: ',sum)

#sum of digits in number