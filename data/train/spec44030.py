import numpy as np 

def function(x):

	e9 = 2
	y0 = x
	paths = []
	try:
		if x <= 2:
			e9 = e9+6
			x = x*4
			x = x+3
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if e9 < 8:
			e9 = 0/e9
			y0 = 5*y0
			paths.append(3)
		else:
			y0 = e9-8
			e9 = e9-e9
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