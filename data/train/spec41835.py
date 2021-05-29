import numpy as np 

def function(x):

	o3 = 6
	y2 = x
	x = x
	paths = []
	try:
		if x > 8:
			y2 = y2+o3
			paths.append(1)
		else:
			o3 = 7/y2
			paths.append(2)
		if x > 9:
			y2 = y2*3
			paths.append(3)
		else:
			o3 = o3/2
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