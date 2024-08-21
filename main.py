from count import *
from graphing import *
def main():
    mode=input("Would you like to create a graph of number syllables?(y/n) ").lower()
    if( mode=="y"):
        graph()
        return
    elif(mode=="n"):
        num=int(input("Number to get Syllables for: "))
        print(count(num))
        return
    else:
        print("Not a valid response.")
        main()
        return
main()