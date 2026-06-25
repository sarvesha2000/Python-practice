import Marvellous as MI #alise (Topan Name)

def main():
    print("enter first number :")
    value1 = int(input())

    print("enter Second number :")
    value2 = int(input())

    ret = MI.Addition(value1,value2)

    print("Addition is :",ret)

if __name__ == "__main__":
    main()