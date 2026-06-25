def BigBazar():
    print("Inside Bigbazar")

    def Amul():
        print("Inside Amul IceCream parlor")


def main():
    BigBazar()  #Allowed
    Amul() #error
    BigBazar.Amul() #error
    

if __name__ == "__main__":
    main()

#symbol table