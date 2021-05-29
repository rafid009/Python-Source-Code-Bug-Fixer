import numpy as np 

def function(x):

	o8 = 5
	a5 = x
	paths = []
	try:
		if x >= 8:
			o8 = x-8
			x = 9*x
			paths.append(1)
		else:
			a5 = a5/3
			x = 8/x
			paths.append(2)
		if x >= 8:
			x = x/3
			paths.append(3)
		else:
			a5 = 5*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))