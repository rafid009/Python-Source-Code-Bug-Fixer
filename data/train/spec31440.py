import numpy as np 

def function(x):

	o7 = x
	c6 = x
	paths = []
	try:
		if o7 > 9:
			c6 = 2+c6
			x = 5*c6
			paths.append(1)
		else:
			c6 = o7/c6
			paths.append(2)
		if o7 <= 7:
			c6 = c6-3
			paths.append(3)
		else:
			c6 = c6+3
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))