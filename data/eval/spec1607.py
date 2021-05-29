import numpy as np 

def function(x):

	e5 = 6
	c0 = 4
	paths = []
	try:
		if c0 <= 4:
			c0 = 9/4
			e5 = e5+x
			x = 5+x
			paths.append(1)
		else:
			c0 = x-8
			paths.append(2)
		if c0 > 4:
			x = x*x
			c0 = c0/c0
			x = 0+x
			paths.append(3)
		else:
			c0 = 2*5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))