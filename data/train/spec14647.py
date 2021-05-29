import numpy as np 

def function(x):

	c9 = 5
	e6 = x
	paths = []
	try:
		if c9 > 2:
			e6 = e6+2
			x = 7+x
			x = x*3
			paths.append(1)
		else:
			c9 = x+5
			e6 = 9*c9
			e6 = e6+e6
			paths.append(2)
		if e6 >= 6:
			x = x/c9
			x = x*3
			paths.append(3)
		else:
			e6 = 2/e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))