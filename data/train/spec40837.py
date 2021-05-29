import numpy as np 

def function(x):

	y0 = 4
	k6 = x
	paths = []
	try:
		if y0 < 0:
			y0 = y0*x
			paths.append(1)
		else:
			k6 = y0-k6
			paths.append(2)
		if y0 <= 9:
			y0 = 1/y0
			y0 = x+5
			paths.append(3)
		else:
			x = x-k6
			y0 = y0*y0
			k6 = 4-8
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))