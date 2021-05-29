import numpy as np 

def function(x):

	c3 = 4
	e3 = x
	paths = []
	try:
		if e3 >= 6:
			c3 = c3-3
			paths.append(1)
		else:
			x = 1*3
			paths.append(2)
		if e3 >= 4:
			e3 = e3+6
			x = x-0
			paths.append(3)
		else:
			c3 = c3+4
			x = x/5
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))