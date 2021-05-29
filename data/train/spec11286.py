import numpy as np 

def function(x):

	e6 = 1
	c3 = 2
	paths = []
	try:
		if x < 2:
			e6 = e6/x
			x = e6-7
			paths.append(1)
		else:
			e6 = e6*1
			c3 = c3-4
			e6 = e6+c3
			paths.append(2)
		if e6 <= 8:
			e6 = e6-e6
			paths.append(3)
		else:
			c3 = c3*1
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