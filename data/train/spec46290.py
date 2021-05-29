import numpy as np 

def function(x):

	x0 = 4
	c9 = x
	paths = []
	try:
		if x >= 8:
			x = x0-7
			paths.append(1)
		else:
			x0 = x0+2
			x0 = x0-x
			c9 = 0-2
			paths.append(2)
		if x <= 4:
			x = 3*7
			x0 = 7+x0
			x0 = 5*2
			paths.append(3)
		else:
			x = 5/x
			x0 = x0+8
			c9 = c9+c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))