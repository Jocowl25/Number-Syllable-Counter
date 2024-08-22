from count import *
from graphing import *
def main():
    mode=input("Would you like to create a graph of number syllables?(y/n) ").lower()
    if( mode=="y"):
        graph()
    elif(mode=="n"):
        num=float(input("Number to get Syllables for: "))
        if(num!=round(num)):
            print("Error: Number is not an integer")
            return
        print(count(int(num)))
    else:
        print("Not a valid response.")
        main()
main()