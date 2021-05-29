import numpy as np 

def function(x):

	c3 = 3
	e5 = 2
	paths = []
	try:
		if c3 <= 1:
			c3 = 7+c3
			x = x/6
			e5 = e5/6
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x > 2:
			x = x-4
			x = e5-x
			e5 = c3-1
			paths.append(3)
		else:
			c3 = x*c3
			e5 = e5-9
			x = 0/3
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