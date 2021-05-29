import numpy as np 

def function(x):

	c3 = 2
	d6 = x
	x = x
	paths = []
	try:
		if c3 <= 5:
			x = 2+x
			d6 = d6/9
			c3 = c3*c3
			paths.append(1)
		else:
			d6 = x-c3
			c3 = 2/c3
			d6 = 7*d6
			paths.append(2)
		if c3 >= 4:
			c3 = c3-4
			c3 = c3+6
			paths.append(3)
		else:
			d6 = d6-0
			d6 = d6*9
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		c3 = d6**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))