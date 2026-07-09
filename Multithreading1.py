import threading

def Display():
    print("Inside Display :",threading.get_ident())


def main():
    print("Inside main :",threading.get_ident())
    Display()

if __name__ == "__main__":
    main()

#ha code threaded ahe yamadhe 1 ch thread ahe
#get_ident - this method will give you id of thread 