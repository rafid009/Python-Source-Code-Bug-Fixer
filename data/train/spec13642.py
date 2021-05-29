import numpy as np 

def function(x):

	e0 = 1
	c5 = x
	paths = []
	try:
		if c5 > 6:
			x = e0-x
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if e0 >= 6:
			c5 = c5*0
			paths.append(3)
		else:
			c5 = 7/1
			c5 = c5*0
			x = x+x
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