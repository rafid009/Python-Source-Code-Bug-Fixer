import numpy as np 

def function(x):

	f1 = 6
	c6 = x
	paths = []
	try:
		if x >= 3:
			f1 = f1/c6
			paths.append(1)
		else:
			f1 = f1+f1
			c6 = 1-c6
			paths.append(2)
		if f1 <= 7:
			f1 = 7/7
			x = x+9
			paths.append(3)
		else:
			f1 = x-c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))