def CheckEven(No):
    return (No % 2 == 0)

def main():
    Data = [13,12,11,20,16,18]

    print("input data is : ",Data)

    FData = list(filter(CheckEven,Data))

    print("DAta after filter : ",FData)

if __name__ == "__main__":
    main()