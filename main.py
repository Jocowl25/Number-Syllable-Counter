from count import *
from graphing import *
def main():
    mode=input("Would you like to create a graph of number syllables?(y/n) ").lower()
    if( mode=="y"):
        graph()
    elif(mode=="n"):
        num=float(input("Number to get Syllables for: "))
        print(count(num))
    else:
        print("Not a valid response.")
        main()
main()