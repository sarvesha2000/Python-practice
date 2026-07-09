CheckEven =lambda No :(No % 2 ==0) #eka line madhe alach pahije

def main():
    value = int(input("Enter Number:"))

    Ret = CheckEven(value) #AFTER COMPILTION RET = (VALUE % 2 == 0)   

    if(Ret == True):
        print("It's Even Number")
    else:
        print("It's Odd Number")

if __name__ == "__main__":
    main()

#Hybrid : Procedural + fUNCTIONAL