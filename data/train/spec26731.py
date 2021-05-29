import numpy as np 

def function(x):

	c7 = 5
	k4 = x
	paths = []
	try:
		if x <= 2:
			c7 = c7*6
			paths.append(1)
		else:
			x = x+x
			x = 0/9
			paths.append(2)
		if x >= 0:
			k4 = 1+k4
			c7 = 8+c7
			paths.append(3)
		else:
			x = k4+6
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))