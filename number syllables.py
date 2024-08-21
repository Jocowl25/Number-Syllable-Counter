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
        plt.yticks(range(max(y)+2))
        plt.xlabel("Number")
        plt.ylabel("Syllables")
        plt.title("Syllable Graph")
        plt.show()
    elif(mode=="n"):
        num=input("Number to get Syllables for: ")
        print(count(num))
    else:
        print("Not a valid response.")
        main()
        return
def count(num):
    strnum=str(num)
    if(len(strnum) % 3 !=0):
        while(len(strnum) % 3 !=0):
            strnum= "0"+strnum
    syl=0 #num of syllables
    end=len(strnum)-1
    if(end>35):
        print("Error: Number too big") #I don't want to deal with varying prefixes past decillion
        return 0
    if(num==0): return 2 #return 2 if 0 because ~edge case~
    for i in range(0,len(strnum)):
        if(strnum[i]!="0"): 
            syl += 1
        else:
            continue
        if(strnum[i]=="7"): #7 is stupid
            syl += 1
        if(i%3==2 and i!=end and strnum[i-2]=="0" and strnum[i-1]=="0"):
                #1000,mil,bil,etc.
                syl+=2
                if(end-i>14): #quadrillion, quintillion, etc.
                    syl+=1
        elif(i%3==1): #check for value in tens place
            if(i>end-3 or strnum[i-1]!="0"):
                syl+=1 # -ty (last 10's place)
            else:
                syl +=3 #-ty + thousand, mil etc.
                if(end-i>14): #quadrillion, quintillion, etc.
                    syl+=1
            if(strnum[i]=="1" and strnum[i+1]!="1"): #check if digit is 1 (for 10) and is not 11
                syl -=1
                if(strnum[i+1]=="2"): #12
                    syl-=1 
        elif(i%3==0): #100's place
                if(i>end-3): #last 100's place
                    syl+=2
                else:
                    syl+=4 #100  + thousand, mil, etc.
                    if(end-i>14): #quadrillion, quintillion, etc.
                        syl+=1
    return syl
main()