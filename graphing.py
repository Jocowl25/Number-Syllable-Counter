import matplotlib.pyplot as plt
from count import *
def graph():
    start=int(input("Start of Range: "))
    end=int(input("End of Range: "))
    print("Counting...")
    x=[]
    y=[]
    for i in range(start,end+1):
        x.append(i)
        y.append(count(i))
    print("Plotting...")
    plt.plot(x,y, color="green", linewidth=0.5, markersize=2,  marker=".",markerfacecolor='black',markeredgecolor='black')
    plt.ticklabel_format(style='plain') 
    plt.yticks(range(max(y)+2))
    plt.ylabel("Syllables")
    plt.title("Syllable Graph")
    plt.show()