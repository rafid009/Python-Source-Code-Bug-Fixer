import numpy as np 

def function(x):

	e5 = x
	c3 = 8
	paths = []
	try:
		if e5 > 8:
			x = x/1
			paths.append(1)
		else:
			e5 = 6+e5
			e5 = e5-7
			e5 = e5/6
			paths.append(2)
		if e5 < 6:
			c3 = x*c3
			paths.append(3)
		else:
			x = x*e5
			x = 9/x
			x = 2-1
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