#----------------------------------------------
#.               List          Tuple
#---------------------------------------------
#Orderd.         Yes            Yes
#Indexed
#Mutable.        Yes            No
#Hetrogeneous.   Yes            Yes
def main():
    Data1 = [10,3.14,True,"Pune"]  #list
    Data2 = (10,3.14,True,"Pune") #Tuple

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])



if __name__ == "__main__":
    main()

#hetrogeneous because dynamically typed
