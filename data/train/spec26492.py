import numpy as np 

def function(x):

	c3 = 4
	j0 = x
	paths = []
	try:
		if j0 >= 7:
			j0 = j0-x
			paths.append(1)
		else:
			x = x*6
			c3 = j0-x
			paths.append(2)
		if c3 <= 8:
			j0 = 6+c3
			j0 = j0*3
			paths.append(3)
		else:
			j0 = x*6
			c3 = 3/j0
			c3 = 0*c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))