import numpy as np 

def function(x):

	o3 = x
	h9 = x
	paths = []
	try:
		if o3 >= 8:
			h9 = h9-1
			o3 = o3*o3
			paths.append(1)
		else:
			o3 = h9/x
			x = 4-0
			paths.append(2)
		if x >= 8:
			x = 8+x
			h9 = h9*9
			x = 6-x
			paths.append(3)
		else:
			h9 = h9/2
			x = 1*x
			o3 = o3-8
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