def CheckEven(No):
    return (No % 2 ==0)
def main():
    value = int(input("Enter Number:"))

    Ret = CheckEven(value)

    if(Ret == True):
        print("Its even number")
    else:
        print("Its odd number")

if __name__ == "__main__":
    main()