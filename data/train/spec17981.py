import numpy as np 

def function(x):

	c3 = 6
	x6 = x
	paths = []
	try:
		if x6 > 7:
			x6 = 5-6
			x6 = x6/x
			paths.append(1)
		else:
			x = x+x
			c3 = x6*c3
			c3 = c3/c3
			paths.append(2)
		if c3 >= 4:
			x6 = 1*x
			x = 6+5
			c3 = c3-4
			paths.append(3)
		else:
			c3 = 5-4
			c3 = c3+x
			x6 = x-7
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