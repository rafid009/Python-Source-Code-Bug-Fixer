import numpy as np 

def function(x):

	e0 = 7
	c3 = 3
	paths = []
	try:
		if e0 >= 6:
			x = x*5
			paths.append(1)
		else:
			x = x+e0
			x = 8+7
			e0 = 7/1
			paths.append(2)
		if e0 < 4:
			c3 = c3/9
			paths.append(3)
		else:
			c3 = e0/c3
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