def getRamAndSD(phoneId,details):
    internal=details.split(" or ")
    variants=[]
    for words in internal:
        temp=words.split(", ")
        try:
            internalsd=temp[0]
            ram=temp[1]
        except IndexError:
            continue
        internalsd=internalsd.split(" ")
        internalsd=internalsd[0]
        ram=ram.split(" ")
        ram=ram[0]
        internalsd=internalsd.split("/")
        ram=ram.split("/")
        temp1=[]
        if len(internalsd)==len(ram):
            for i in range(0,len(ram)):
                temp1.append(phoneId)
                temp1.append(internalsd[i])
                temp1.append(ram[i])
            variants.append(temp1)
        else:
            if len(ram)==1:
                for j in range(0,len(internalsd)):
                    temp2=[]
                    temp2.append(phoneId)
                    temp2.append(internalsd[j])
                    temp2.append(ram[0])
                    variants.append(temp2)
            if len(internalsd)==1:
                for j in range(0,len(ram)):
                    temp2=[]
                    temp2.append(phoneId)
                    temp2.append(internalsd[0])
                    temp2.append(ram[j])
                    variants.append(temp2)
    return variants
