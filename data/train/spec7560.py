import numpy as np 

def function(x):

	o8 = 2
	k2 = 3
	paths = []
	try:
		if o8 < 8:
			k2 = 8-3
			paths.append(1)
		else:
			o8 = 2/o8
			paths.append(2)
		if k2 > 6:
			k2 = o8*k2
			x = 4*9
			k2 = 2*x
			paths.append(3)
		else:
			x = x/6
			o8 = 9*k2
			x = x-1
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