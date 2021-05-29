import numpy as np 

def function(x):

	n2 = x
	c6 = x
	paths = []
	try:
		if c6 <= 7:
			x = x+x
			c6 = 7*c6
			paths.append(1)
		else:
			c6 = 7*c6
			paths.append(2)
		if x >= 0:
			c6 = 7-7
			n2 = c6-8
			c6 = x+x
			paths.append(3)
		else:
			x = c6+9
			n2 = n2-4
			c6 = 0-c6
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))