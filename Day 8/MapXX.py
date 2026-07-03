CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No + 1


def main():
    Data = [13,12,11,20,16,18]

    print("input data is : ",Data)

    FData = list(filter(CheckEven,Data))

    print("DAta after filter : ",FData)

    MData = list(map(Increment,FData))

    print("DAta after map : ",MData)

if __name__ == "__main__":
    main()