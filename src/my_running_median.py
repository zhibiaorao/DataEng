from re import split

def insertA(n, sorted_list,i):
    N = len(sorted_list);
    if N == 0: return [],i;
    elif N ==1:
        if n < sorted_list[0]: return [],i;
        else: return [],i+1;
        pass
    if n < sorted_list[N/2]:
        sorted_list,i = insertA(n,sorted_list[:N/2],i)
    else:
        sorted_list,i = insertA(n,sorted_list[N/2:],i)
        i = i + N/2;
        pass
    return sorted_list,i

lineword = []
ReadNo = []
with open("C:\Users\zhibiao\Desktop\DataEng-master\DataEng-master\wc_input\test.txt","rU") as files:
    for line in files:
        line = line.strip().lower()
        for word in split("[^a-zA-Z']+", line):
            if word:
                lineword.append(word)

        WordNo = len(lineword)
        a,i = insertA(WordNo, ReadNo,0);
        ReadNo= ReadNo[:i]+ [WordNo] +ReadNo[i:]
        N = len(ReadNo)
        if N%2 ==0: print((ReadNo[N/2] + ReadNo[N/2-1])/2.0)
        else:print(ReadNo[N/2])
        lineword = []





