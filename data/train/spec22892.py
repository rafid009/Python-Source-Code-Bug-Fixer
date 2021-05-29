import numpy as np 

def function(x):

	o3 = x
	x5 = x
	x = 5
	paths = []
	try:
		if x5 >= 8:
			x = 5+o3
			o3 = o3/1
			x5 = 8+9
			paths.append(1)
		else:
			x5 = 5+x5
			o3 = o3*9
			x = x5+2
			paths.append(2)
		if x5 <= 1:
			x = 1-x
			x5 = o3*6
			paths.append(3)
		else:
			x5 = x5+9
			x = 6/x
			x = 8+o3
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