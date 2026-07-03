#selection
#if

x = 50
if (x > 20):
    print("Greater")


#if-else
if (x > 60):
    print("Greater")
else:
    print("smaller")


#if-elif-else
if (x > 60):
    print("Greater")
elif (x == 50):
    print("Equal")
else:
    print("smaller")

#nested if

if (x > 40):
    if (x < 60):
        print("x is between 40 and 60")
    else:
        print("x is greater than or equal to 60")


#logical operators

(x > 40) and (x < 55)
print("Between 40 and 55")

(x > 40) or (x > 55)
print("Any one condition is matched")

not (x == 60)
print("No")