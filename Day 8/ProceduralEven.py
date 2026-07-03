def CheckEven(No):

    if (No % 2 == 0):
        print("Even")
    else:
        print("Odd")



def main():
    Value =int(input("Enter a number : "))

    CheckEven(Value)
    #ret = CheckEven(Value)
    #print(ret)



if __name__ == "__main__":
    main()

