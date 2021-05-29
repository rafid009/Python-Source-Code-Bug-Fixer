import numpy as np 

def function(x):

	c5 = x
	a1 = 7
	paths = []
	try:
		if c5 > 4:
			a1 = 4-a1
			a1 = a1+c5
			a1 = c5+4
			paths.append(1)
		else:
			x = c5+4
			c5 = c5*7
			c5 = x*0
			paths.append(2)
		if a1 < 4:
			c5 = 3+c5
			a1 = a1/a1
			paths.append(3)
		else:
			a1 = 5-a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))