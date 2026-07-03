print("------Ticket Pricing Software------")

print("Enter your age: ")
Age = int(input())

if(Age <= 5):
    print("you are free")

elif(Age > 5 and Age <= 18):
    print("ticket price is 900")

elif(Age > 18 and Age <= 40):
    print("ticket price is 1200")

else:
    print("tiket price is 500")