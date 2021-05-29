import numpy as np 

def function(x):

	a9 = x
	y0 = 4
	paths = []
	try:
		if y0 < 5:
			a9 = a9+a9
			y0 = y0*3
			paths.append(1)
		else:
			y0 = 5/8
			paths.append(2)
		if x <= 5:
			x = x+1
			a9 = a9+3
			paths.append(3)
		else:
			y0 = 2-y0
			y0 = 5-9
			a9 = x+x
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