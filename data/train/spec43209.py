import numpy as np 

def function(x):

	k4 = x
	c3 = x
	paths = []
	try:
		if x < 3:
			c3 = c3+0
			x = x+k4
			k4 = 5*k4
			paths.append(1)
		else:
			k4 = k4+7
			paths.append(2)
		if x < 0:
			k4 = 0/k4
			k4 = k4-5
			paths.append(3)
		else:
			c3 = k4+c3
			c3 = 4+4
			x = x*9
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