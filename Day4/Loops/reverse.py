n = int(input())

while n > 0:
    digit = n % 10
    print(digit)
    n //= 10

    #print reverse of a number