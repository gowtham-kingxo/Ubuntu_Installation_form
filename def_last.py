def find_last(a,b):
	c=0
	d=-1
	while c!=-1:
		c=a.find(b,c+1)
		print (c)
		d=c
		c=a.find(b,c+1)
		print (c)
	
find_last('111111111', '1')