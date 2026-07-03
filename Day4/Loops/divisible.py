#no. divisible by 3 bet 1 to 100

count = 0

for i in range(1,101):
    if i % 3 == 0:
        count += 1

print("Count: ",count)