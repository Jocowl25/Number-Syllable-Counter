def count(num):
    syllables=0 #num of syllables
    strnum=str(num)
    dot=strnum.find(".")
    if(round(num)!=num):
        return 0
        #return 1+count(int(strnum[:dot]))+count(int(strnum[dot+1:]))
    else:
        strnum=str(int(num))
    if(num<0):
        syllables += 3
        strnum=str(abs(num))
    if(len(strnum) % 3 !=0):
        while(len(strnum) % 3 !=0):
            strnum= "0"+strnum
    end=len(strnum)-1
    if(end>35):
        print("Error: Number too big") #I don't want to deal with varying prefixes past decillion
        return 0
    if(num==0): return 2 #return 2 if 0 because ~edge case~
    for i in range(0,len(strnum)):
        if(strnum[i]!="0"): 
            syllables += 1
        else:
            continue
        if(strnum[i]=="7"): #7 is stupid
            syllables += 1
        if(i%3==2 and i!=end and strnum[i-2]=="0" and strnum[i-1]=="0"):
                #1000,mil,bil,etc.
                syllables+=2
                if(end-i>14): #quadrillion, quintillion, etc.
                    syllables+=1
        elif(i%3==1): #check for value in tens place
            if(i>end-3 or strnum[i-1]!="0"):
                syllables+=1 # -ty (last 10's place)
            else:
                syllables +=3 #-ty + thousand, mil etc.
                if(end-i>14): #quadrillion, quintillion, etc.
                    syllables+=1
            if(strnum[i]=="1" and strnum[i+1]!="1"): #check if digit is 1 (for 10) and is not 11
                syllables -=1
                if(strnum[i+1]=="2"): #12
                    syllables-=1 
        elif(i%3==0): #100's place
                if(i>end-3): #last 100's place
                    syllables+=2
                else:
                    syllables+=4 #100  + thousand, mil, etc.
                    if(end-i>14): #quadrillion, quintillion, etc.
                        syllables+=1
    return syllables
