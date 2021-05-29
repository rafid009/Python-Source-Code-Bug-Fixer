import numpy as np 

def function(x):

	y0 = x
	e0 = 5
	x = x
	paths = []
	try:
		if e0 < 1:
			x = 8-x
			y0 = y0+2
			e0 = 3-0
			paths.append(1)
		else:
			y0 = y0+8
			paths.append(2)
		if y0 <= 1:
			e0 = y0-e0
			paths.append(3)
		else:
			e0 = 2/5
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		y0 = e0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))