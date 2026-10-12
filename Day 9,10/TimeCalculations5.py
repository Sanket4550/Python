import time
def Factorial(Num):
    Ans = 1

    for i in range(1,Num+1):
        Ans = Ans * i
    return Ans


def main():
    Value = int(input("Enter number : "))

    start_time = time.perf_counter()
    Ret = Factorial(Value)

    end_time = time.perf_counter()
    print(f"Factorial of {Value} is {Ret}")

    print(f"Time required is : {end_time-start_time : .5f} seconds")

if __name__ == "__main__":
    main()