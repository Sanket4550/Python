CheckEven = lambda No : (No % 2 == 0)

    



def main():
    Value =int(input("Enter a number : "))

    Ret = CheckEven(Value) #Ret = (Value % 2 == 0)
    
    if (Ret == True):
        print("Even Number")
    else:
        print("Odd Number")
    
    



if __name__ == "__main__":
    main()

