import numpy as np 

def function(x):

	o4 = x
	u0 = 6
	paths = []
	try:
		if u0 >= 3:
			u0 = 8/o4
			u0 = 2/u0
			x = x*o4
			paths.append(1)
		else:
			u0 = x*u0
			o4 = 6+o4
			paths.append(2)
		if u0 < 2:
			u0 = u0*u0
			o4 = 6*o4
			u0 = 9-u0
			paths.append(3)
		else:
			u0 = 4/u0
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))