import numpy as np 

def function(x):

	u0 = 0
	o9 = x
	paths = []
	try:
		if x > 5:
			o9 = o9-4
			u0 = 8+u0
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if o9 < 2:
			u0 = 3*u0
			paths.append(3)
		else:
			x = u0-0
			x = x-1
			o9 = o9+6
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