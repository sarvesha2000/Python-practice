def Calculation(No1,No2):
    Mult = No1 * No2
    Div = No1/No2
    return Mult,Div


def main():
    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter Second number :"))

    ret1,ret2 = Calculation(Value1,Value2)
    print("Multiplication is :",ret1)
    print("Division is :",ret2)

if __name__ == "__main__":
    main()

#symbol table