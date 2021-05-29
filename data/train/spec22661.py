import numpy as np 

def function(x):

	c9 = 2
	j0 = 6
	paths = []
	try:
		if c9 < 4:
			c9 = c9*c9
			j0 = j0+6
			paths.append(1)
		else:
			c9 = 5-x
			paths.append(2)
		if c9 > 9:
			j0 = 7+4
			j0 = 5/c9
			x = x/5
			paths.append(3)
		else:
			c9 = c9/9
			j0 = 2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))