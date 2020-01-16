def ungapped(seq1,seq2):
    gaps1=len(seq2)
    for i in range(gaps1):
        seq1="-"+seq1
    for i in range (len(seq1)):
        print (seq1)
        print (seq2)
        seq2="-"+seq2
    return
#This program print all the ungapped combinations between 2 sequences 

                
                   
