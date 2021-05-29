import numpy as np 

def function(x):

	o3 = 9
	e4 = x
	x = x
	paths = []
	try:
		if o3 < 7:
			e4 = 3-x
			paths.append(1)
		else:
			o3 = o3-x
			paths.append(2)
		if e4 <= 5:
			e4 = 7+e4
			o3 = 9*x
			paths.append(3)
		else:
			o3 = x+o3
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