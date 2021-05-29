import numpy as np 

def function(x):

	e0 = 4
	l8 = 5
	paths = []
	try:
		if x < 8:
			x = l8+l8
			paths.append(1)
		else:
			l8 = 2-l8
			x = x/l8
			e0 = e0+e0
			paths.append(2)
		if x <= 6:
			x = x*2
			paths.append(3)
		else:
			e0 = 3/4
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