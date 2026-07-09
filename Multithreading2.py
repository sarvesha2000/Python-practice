import threading

def Display():
    print("Inside Display :",threading.get_ident())


def main():
    print("Inside main :",threading.get_ident())

    tobj = threading.Thread(target = Display) #yane thread create hoto start hot nahi 
    
    tobj.start() 

if __name__ == "__main__":
    main()