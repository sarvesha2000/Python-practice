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

