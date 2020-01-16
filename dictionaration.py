def scoring_matrix(archivo):
    f =open(archivo)
    aa=""
    list_aa=[]
    list_aa2=[]
    dic_aa={}
    for line in f:

        line=line.rstrip()
        if aa=="":
            aa= line.split()
        else:
            list_aa.append(line.split())
    for i in list_aa:
            if len(i)!=0:
                list_aa2.append(i)
    var=len(aa)
    for i in range(len(list_aa2)):
        for j in range(var,0,-1):
            
            dic_aa[list_aa2[i][0]+aa[20-j]]=list_aa2[i][20-j+1]
        var-=1
    f.close()
    return dic_aa
#In this program the input is a text file which contains a 20x20 matrix , and the output
#is a dictionary which contains the 210 possible combinations and the score of each combination

 

