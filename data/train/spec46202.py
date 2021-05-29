import numpy as np 

def function(x):

	c4 = 2
	n2 = 4
	paths = []
	try:
		if n2 > 0:
			x = 0/x
			n2 = 9-n2
			c4 = 8-4
			paths.append(1)
		else:
			c4 = c4-4
			n2 = c4*c4
			paths.append(2)
		if n2 > 5:
			x = c4/4
			x = 7*x
			paths.append(3)
		else:
			n2 = 2-3
			c4 = n2+x
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))