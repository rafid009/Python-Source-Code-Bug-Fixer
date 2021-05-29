import numpy as np 

def function(x):

	e4 = 2
	n0 = x
	paths = []
	try:
		if x <= 2:
			x = n0/9
			x = x+x
			x = 8*4
			paths.append(1)
		else:
			n0 = x+e4
			e4 = 1/e4
			paths.append(2)
		if n0 > 8:
			x = x-0
			e4 = e4/9
			paths.append(3)
		else:
			x = e4-3
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