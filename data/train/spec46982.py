import numpy as np 

def function(x):

	o8 = 2
	a9 = x
	paths = []
	try:
		if o8 < 9:
			o8 = o8-a9
			a9 = 3/8
			x = x+6
			paths.append(1)
		else:
			a9 = 4-a9
			a9 = 9*3
			x = x-8
			paths.append(2)
		if a9 < 9:
			x = 3*x
			a9 = 6-9
			paths.append(3)
		else:
			x = a9+0
			a9 = a9/x
			a9 = 1-o8
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