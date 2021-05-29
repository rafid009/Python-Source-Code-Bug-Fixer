import numpy as np 

def function(x):

	y0 = x
	f9 = 6
	paths = []
	try:
		if y0 > 1:
			y0 = 3+y0
			y0 = y0/f9
			f9 = y0/f9
			paths.append(1)
		else:
			x = 4+x
			y0 = y0-5
			paths.append(2)
		if x < 6:
			f9 = f9+4
			paths.append(3)
		else:
			y0 = 6-y0
			x = 4*6
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