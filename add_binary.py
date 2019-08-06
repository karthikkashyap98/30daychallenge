def add_binary(a,b):
	#your code here
	c= []
	s = a+b
	flag=0
	while(1):    
		c.append(s%2)
		s = s//2
		if s==1:
			c.append(s)
			break
	res = int("".join(map(str, c)))
	return res

sup = add_binary(1,1)
print(sup)    