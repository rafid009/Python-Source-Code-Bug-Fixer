import numpy as np 

def function(x):

	c5 = x
	n6 = x
	paths = []
	try:
		if c5 >= 7:
			n6 = n6+3
			c5 = c5+c5
			x = 8*1
			paths.append(1)
		else:
			x = 2-n6
			paths.append(2)
		if x < 9:
			c5 = 4+n6
			paths.append(3)
		else:
			x = 2*c5
			n6 = 1/x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))