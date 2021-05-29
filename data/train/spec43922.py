import numpy as np 

def function(x):

	o3 = 9
	g4 = x
	paths = []
	try:
		if o3 > 1:
			x = g4*5
			g4 = g4+9
			paths.append(1)
		else:
			x = x-4
			g4 = 9+g4
			paths.append(2)
		if x > 9:
			x = o3/2
			o3 = o3+o3
			paths.append(3)
		else:
			g4 = 9/2
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