import numpy as np 

def function(x):

	v4 = 0
	y0 = x
	paths = []
	try:
		if y0 < 5:
			v4 = 9*v4
			v4 = v4-x
			y0 = y0*y0
			paths.append(1)
		else:
			x = 6+8
			y0 = y0+7
			v4 = 9*1
			paths.append(2)
		if x < 9:
			v4 = 1-v4
			x = x+v4
			paths.append(3)
		else:
			y0 = y0-x
			x = x/5
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