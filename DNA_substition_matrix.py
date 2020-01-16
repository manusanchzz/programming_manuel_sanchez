def substitution_matrix(seq1,seq2):
    alig=len(seq1)*2
    letters=["A","T","G","C"]
    scA= (seq1.count("A")+ seq2.count("A"))/alig
    scT= (seq1.count("T")+ seq2.count("T"))/alig
    scG= (seq1.count("G")+ seq2.count("G"))/alig
    scC= (seq1.count("C")+ seq2.count("C"))/alig
    sc=[scA,scT,scG,scC]
    lines=[]
    for i in range(len(seq1)):
        lines.append((seq1[i]+seq2[i]))

    matrix=[]
    for i in range (4):
        file=[]
        for j in range(4):
            file.append(int((((lines.count(letters[i]+letters[j])+lines.count(letters[j]+letters[i]))/len(seq1))/(sc[i]*sc[j]))))
        matrix.append(file)
        
    for i in range(4):
        matrix[i][i]=int(matrix[i][i]/2)
    print (["X"]+letters)
    for i in range (4):
        print ((letters[i],matrix[i]),end="\n\r")
    residues="ATGC"
    score=0
    for i in range(len(seq1)):
        score =score + matrix[residues.find(seq1[i])][residues.find(seq2[i])]   

        
    return score
#This program makes a substitution matrix of an alingment between two DNA sequences
# and compute the score of the alignment based on that matrix
# Also print the matrix 
            
