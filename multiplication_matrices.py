def multmatrix(matrix1,matrix2):
	matrix12=[]
	#We created a matrix filled with zeros to refill later the result of the product 	       
	for i in range(len(matrix1)):
		line=[]
		for j in range(len(matrix2[0])):
		       line.append(0)
		matrix12.append(line)
	#iterate through rows of matrix1
	for i in range(len(matrix1)):
		#iterate through columns of matrix2
		for j in range(len(matrix2[0])):
		       #iterate through rows of matrix2
		       for k in range(len(matrix2)):
			       matrix12[i][j]+=matrix1[i][k]*matrix2[k][j]
	for r in matrix12:
	#pirnt the matrix resut of the product
		print (r)
	
	return
