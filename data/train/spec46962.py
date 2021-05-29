import numpy as np 

def function(x):

	e6 = x
	c9 = 9
	paths = []
	try:
		if x < 4:
			x = 4+x
			x = x-3
			paths.append(1)
		else:
			e6 = e6-5
			e6 = 3/6
			paths.append(2)
		if x <= 7:
			x = x/7
			e6 = e6+e6
			paths.append(3)
		else:
			x = c9*8
			c9 = 3*8
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