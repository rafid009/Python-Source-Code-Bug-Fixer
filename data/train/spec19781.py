import numpy as np 

def function(x):

	c0 = 8
	g6 = x
	paths = []
	try:
		if c0 < 9:
			x = g6/8
			paths.append(1)
		else:
			x = 6+g6
			c0 = x+1
			x = x/6
			paths.append(2)
		if x > 7:
			c0 = c0*3
			paths.append(3)
		else:
			c0 = 8+9
			c0 = c0/1
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))