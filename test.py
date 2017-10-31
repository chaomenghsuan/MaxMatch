def maxmatch(sentence, dictionary):
    lst=[]
    while sentence:
        for i in range(len(sentence),0,-1):
            firstword = sentence[0:i]
            if firstword in dictionary:
                lst.append(firstword)
                sentence = sentence[i: ]
    return lst

#D=['我','你','吃','苹果','桃子']
#print(maxmatch('我吃苹果', D))