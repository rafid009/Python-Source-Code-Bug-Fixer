import numpy as np 

def function(x):

	o3 = 2
	k0 = x
	paths = []
	try:
		if o3 >= 7:
			o3 = 8/o3
			x = x/2
			paths.append(1)
		else:
			o3 = 9/3
			paths.append(2)
		if o3 >= 1:
			x = 7-x
			paths.append(3)
		else:
			o3 = o3/3
			o3 = o3-x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))