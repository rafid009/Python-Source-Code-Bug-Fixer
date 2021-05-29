import numpy as np 

def function(x):

	h6 = 4
	c7 = 5
	paths = []
	try:
		if c7 > 8:
			h6 = h6*7
			paths.append(1)
		else:
			h6 = x*h6
			x = 0*x
			paths.append(2)
		if x <= 4:
			x = 2*h6
			x = x-6
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		c7 = h6**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))