def Factorial(Num):
    Ans = 1

    for i in range(1,Num+1):
        Ans = Ans * i
    return Ans


def main():
    Value = int(input("Enter number : "))
    Ret = Factorial(Value)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()