import numpy as np 

def function(x):

	c7 = x
	g1 = x
	paths = []
	try:
		if x >= 4:
			x = x/9
			paths.append(1)
		else:
			x = x*x
			x = c7*x
			g1 = g1-7
			paths.append(2)
		if x >= 4:
			c7 = 6+c7
			g1 = 4*g1
			paths.append(3)
		else:
			c7 = 4/c7
			c7 = c7+4
			x = x-9
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))