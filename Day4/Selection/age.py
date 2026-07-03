print("enter a age: ")
a = int(input())

if (a >= 0 and a <= 12):
    print("Child")
elif (a >= 13 and a <= 17):
    print("Teenager")
elif (a >= 18 and a <= 60):
    print("Adult")
else:
    print("Senior Citizen")