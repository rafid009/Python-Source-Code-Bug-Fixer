import numpy as np 

def function(x):

	g7 = 4
	o3 = 6
	paths = []
	try:
		if x < 2:
			g7 = 0-g7
			o3 = x-o3
			o3 = 1+o3
			paths.append(1)
		else:
			o3 = o3*x
			x = 5-x
			o3 = o3-3
			paths.append(2)
		if o3 < 8:
			o3 = o3/9
			o3 = o3*3
			paths.append(3)
		else:
			o3 = o3+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))