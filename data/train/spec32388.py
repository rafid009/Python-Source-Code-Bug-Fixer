import numpy as np 

def function(x):

	h2 = 4
	o3 = x
	paths = []
	try:
		if o3 >= 9:
			x = o3-h2
			h2 = 8/7
			paths.append(1)
		else:
			x = x*h2
			paths.append(2)
		if x >= 5:
			x = 6+o3
			o3 = o3+8
			o3 = o3/9
			paths.append(3)
		else:
			x = x+6
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