import numpy as np 

def function(x):

	y0 = x
	w3 = 0
	paths = []
	try:
		if x <= 9:
			y0 = y0+w3
			y0 = x+7
			paths.append(1)
		else:
			y0 = x*y0
			w3 = y0+0
			paths.append(2)
		if x <= 3:
			y0 = y0+9
			paths.append(3)
		else:
			x = 5*x
			y0 = y0-x
			w3 = 0-9
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