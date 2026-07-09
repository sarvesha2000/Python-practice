CheckEven = lambda No:(No % 2 == 0)

Increment = lambda No: No + 1

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is :",Data)

    FData =list(filter(CheckEven,Data)) 

    print("Data after filer :",FData)

    MData = list(map(Increment,FData))

    print("Data after map :",MData)

   
if __name__ == "__main__":
    main()

#functions are considerd as first class object in python