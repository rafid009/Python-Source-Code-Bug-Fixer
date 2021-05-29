import numpy as np 

def function(x):

	n1 = 7
	c1 = 4
	x = 1
	paths = []
	try:
		if x > 0:
			n1 = n1-x
			n1 = n1/n1
			n1 = n1*2
			paths.append(1)
		else:
			x = 3+1
			n1 = n1/n1
			x = x*3
			paths.append(2)
		if n1 > 1:
			n1 = n1+c1
			x = x*1
			c1 = 1-9
			paths.append(3)
		else:
			c1 = 5-n1
			x = n1+x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		n1 = c1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))