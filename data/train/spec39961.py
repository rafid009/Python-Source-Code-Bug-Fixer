import numpy as np 

def function(x):

	c1 = 6
	k4 = x
	paths = []
	try:
		if k4 <= 6:
			x = k4/3
			x = 5*x
			paths.append(1)
		else:
			x = 5-x
			k4 = k4*2
			k4 = 3+c1
			paths.append(2)
		if c1 >= 8:
			k4 = k4*c1
			k4 = 2*k4
			k4 = c1/k4
			paths.append(3)
		else:
			x = 2-c1
			k4 = x*6
			k4 = k4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))