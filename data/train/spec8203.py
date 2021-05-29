import numpy as np 

def function(x):

	o2 = x
	o3 = x
	paths = []
	try:
		if x >= 4:
			x = 0*x
			o3 = o3*5
			paths.append(1)
		else:
			o2 = 3/7
			o3 = 4-x
			paths.append(2)
		if x > 4:
			o3 = o3-0
			paths.append(3)
		else:
			o3 = o3+3
			o3 = 6-0
			o3 = 0-o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))