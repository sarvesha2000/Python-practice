no = 11       #defination

def Display():
    global no #defination.telling interpreter i dont want to create new no i want to refer global no
    no = 21
    print("From Display :",no) #nearest no

print("Before :",no)
Display()
print("After :",no)

#global - delcare 