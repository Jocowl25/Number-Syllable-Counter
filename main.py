from count import *
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
def main():
    mode=input("Would you like to create a graph of number syllables?(y/n) ").lower()
    if( mode=="y"):
        start=int(input("Start of Range: "))
        end=int(input("End of Range: "))
        print("Counting...")
        x=[]
        y=[]
        for i in range(start,end):
            x.append(i)
            y.append(count(i))
        print("Plotting...")
        plt.plot(x,y, color="green", linewidth=0.5, markersize=2,  marker=".",markerfacecolor='black',markeredgecolor='darkgreen')
        plt.ticklabel_format(style='plain') 
        plt.yticks(range(max(y)+2))
        plt.ylabel("Syllables")
        plt.title("Syllable Graph")
        plt.show()
    elif(mode=="n"):
        num=int(input("Number to get Syllables for: "))
        print(count(num))
    else:
        print("Not a valid response.")
        main()
        return
main()