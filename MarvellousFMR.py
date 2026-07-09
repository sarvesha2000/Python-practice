

CheckEven=lambda No:(No % 2 == 0)

Increment =lambda No: No + 1

Addition = lambda No1,No2:No1 + No2

def filterX(Task,Elements):
    result = []
    for no in Elements:
        Ret = Task(no) #checkeven(no)

        if(Ret == True):
            result.append(no)
    return result
def mapX(Task,Elements):
    Result = []
    for no in Elements:
        Ret = Task(no) #Increment
        Result.append(Ret)

    return Result
def reduceX(Task,Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum




def main():
    Data = [13,12,8,10,11,20]

    print("Input data is :",Data)

    FData =list(filterX(CheckEven,Data)) 

    print("Data after filer :",FData)

    MData = list(mapX(Increment,FData))

    print("Data after map :",MData)

    RData = reduceX(Addition,MData)

    print("Data after Reduce:",RData)

   
if __name__ == "__main__":
    main()