#UTC time :unix ni 1 Jan 1970 pasun attaparyant calculate kelela time(Elapsed time)
import time


def Factorial(No):
    fact = 1

    for i in range(1,No +1):
        fact = fact * i

    return fact

def main():

    Value = int(input("Enter number :"))
    start_Time = time.time()

    ret = Factorial(Value)

    end_Time = time.time()

    print(f"Time required is : {end_Time - start_Time : .5f} Seconds")

    print(f"Factorial  of {Value} is {ret}") 

if __name__ == "__main__":
    main()