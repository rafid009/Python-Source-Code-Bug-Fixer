import numpy as np 

def function(x):

	j0 = x
	c1 = 3
	paths = []
	try:
		if j0 <= 6:
			x = j0*1
			c1 = 3-2
			x = x+6
			paths.append(1)
		else:
			x = x+x
			j0 = c1*x
			j0 = j0*9
			paths.append(2)
		if j0 < 7:
			x = 6-x
			x = x*2
			paths.append(3)
		else:
			j0 = c1/j0
			x = 6*x
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