import numpy as np 

def function(x):

	c4 = 4
	r5 = 5
	paths = []
	try:
		if c4 <= 2:
			c4 = 6+3
			c4 = 9+c4
			r5 = 7+r5
			paths.append(1)
		else:
			r5 = r5-r5
			r5 = 5+r5
			r5 = 3-2
			paths.append(2)
		if x >= 1:
			x = 5*c4
			c4 = 3/c4
			paths.append(3)
		else:
			c4 = c4/1
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