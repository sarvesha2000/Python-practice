#Accept :Multiple parameters 
#Return :One value

def Marvellous(value1,value2) :
    print("Inside Marvellous",value1,value2)
    return 21

def main():
    ret = Marvellous(10,20)
    print("return value is :",ret)

if __name__ == "__main__":
    main()
