import numpy as np 

def function(x):

	o9 = 0
	z0 = 4
	paths = []
	try:
		if z0 <= 1:
			x = x-2
			x = z0-x
			paths.append(1)
		else:
			x = x*5
			x = x+1
			x = 6/x
			paths.append(2)
		if x <= 0:
			o9 = 8*o9
			o9 = o9-8
			paths.append(3)
		else:
			o9 = 8*o9
			o9 = 2-x
			x = x+7
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