rows = "ARNDCQEGHILKMFPSTWYV"
cols = "ARNDCQEGHILKMFPSTWYV"


def score(seq1,seq2,matrix):
    def dicti(archivo):
        list_aa=[]
        list_aa2=[]
        dic_aa={}
        f=open(archivo)
        for i in f:
            list_aa.append(i.split())
        for i in list_aa:
            if len (i)!=0:
                list_aa2.append(i)
        for i in range(len(list_aa2)):
            for j in range(len(list_aa2[i])):
                dic_aa[rows[i]+cols[j]]=list_aa2[i][j]
        return dic_aa
    dic_aa=dicti(matrix)
    score=0
    keys=dic_aa.keys()
    for i in range (len(seq1)):
        if (seq1[i]+seq2[i]) in keys:
            score=score+ int(float((dic_aa[seq1[i]+seq2[i]])))
        else:
            score-=1
    return score

        

    
        
