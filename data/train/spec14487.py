import numpy as np 

def function(x):

	c4 = 2
	n1 = 0
	paths = []
	try:
		if c4 >= 8:
			c4 = 2+c4
			c4 = c4*8
			paths.append(1)
		else:
			x = x*0
			x = 5-6
			n1 = n1/c4
			paths.append(2)
		if x > 9:
			c4 = 0+c4
			paths.append(3)
		else:
			c4 = c4+2
			c4 = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))