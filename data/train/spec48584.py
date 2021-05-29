import numpy as np 

def function(x):

	y0 = x
	e1 = x
	paths = []
	try:
		if e1 >= 3:
			x = e1+x
			paths.append(1)
		else:
			x = x*2
			y0 = y0-3
			x = 3-x
			paths.append(2)
		if e1 < 8:
			x = x/7
			e1 = e1+6
			e1 = 2/y0
			paths.append(3)
		else:
			e1 = 9+e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))