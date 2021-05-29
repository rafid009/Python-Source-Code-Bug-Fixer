import numpy as np 

def function(x):

	a1 = 3
	c6 = x
	x = 6
	paths = []
	try:
		if c6 <= 9:
			x = x+c6
			x = a1-x
			paths.append(1)
		else:
			x = c6+x
			c6 = c6*6
			paths.append(2)
		if x > 6:
			x = x+9
			x = 9/x
			paths.append(3)
		else:
			a1 = 1/a1
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