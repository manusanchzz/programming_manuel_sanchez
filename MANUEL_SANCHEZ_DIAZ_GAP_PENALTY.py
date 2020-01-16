def exam (file_matrix,file_alignments):
    def dicti (file_matrix):
        aa="ARNDCQEGHILKMFPSTWYV"
        list_aa=[]
        list_aa2=[]
        dic_aa={}
        f=open(file_matrix,"r")
        for i in f:
            i=i.rstrip()
            if i[0]!= "M":
                list_aa.append(i.split())
        for i in list_aa:
            if len (i)!=0:
                list_aa2.append(i)
        for i in range(len(list_aa2)):
            for j in range(len(list_aa2[i])):
                dic_aa[aa[i]+aa[j]]=list_aa2[i][j]
        return dic_aa
    def alig(file_alignments):
        f=open(file_alignments,"r")
        pair_alignments=[]
        for i in f:
            
            i=i.rstrip()
            pair_alignments.append(i)
        
        pair_alignments2=[]
            
        for i in range(0,len(pair_alignments),4):
            pair_alignments2.append([pair_alignments[i+1],pair_alignments[i+3]])
        
        return pair_alignments2
    
    def score(sc):
        final_score=[]
        dic_aa=dicti(file_matrix)
        keys=dic_aa.keys()
        for i in alig(file_alignments):
            score=0
            
            seq1=i[0]
            
            seq2=i[1]
            g=0
            for i in range (len(seq1)):
                if (seq1[i]+seq2[i])  in keys:
                    score=score+ float((dic_aa[seq1[i]+seq2[i]]))
                    if g!=0:
                        score+= -2 -(g-1)* 0.5
                        g=0
                    
                elif (seq2[i]+seq1[i]) in keys:
                    score=score+ float((dic_aa[seq2[i]+seq1[i]]))
                    if g!=0:
                        score+= -2 -(g-1)* 0.5
                        g=0
                else:
                    g+=1
            final_score.append(score)
        return final_score
    final_alignments=alig(file_alignments)
    final_score=score(final_alignments)
    for i in range (len(final_alignments)):
        print (final_alignments[i][0])
        print (final_alignments[i][1])
        print ("The score of this alignment is " , final_score[i])
        
    
            
    
        
        

