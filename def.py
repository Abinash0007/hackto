def arr(A):
	xor = 0
	count=0
	for i in A:
		xor ^= (1<<i)
	for i in A:		
		if (xor & (1<<i) !=0):
			count+=1
			xor ^= (1<<i)
	return count
A =[5, 8, 2, 5, 8, 2, 8, 5, 1, 8, 2 ]
print (arr(A))
