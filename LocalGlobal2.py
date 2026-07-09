
No = 11       #Global Variable 

def Display():
    a = 21    #Local Variable
    print("From Display :",No)
    print("From Display Value of a is :",a)

def Demo():
     print("Value of a is:",a)
     print("From Demo :",No)

Display()
Demo()