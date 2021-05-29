import numpy as np 

def function(x):

	o3 = 4
	y0 = x
	paths = []
	try:
		if y0 > 2:
			o3 = o3*2
			o3 = y0/9
			paths.append(1)
		else:
			x = 6/x
			y0 = y0*o3
			paths.append(2)
		if y0 > 6:
			y0 = 4-x
			y0 = 0-0
			paths.append(3)
		else:
			o3 = x/o3
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