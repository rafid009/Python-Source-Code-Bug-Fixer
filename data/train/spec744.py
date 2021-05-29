import numpy as np 

def function(x):

	x1 = x
	o7 = x
	paths = []
	try:
		if o7 < 8:
			o7 = 0*o7
			paths.append(1)
		else:
			x1 = 9-x
			x = 6-o7
			paths.append(2)
		if x > 7:
			x = x-3
			paths.append(3)
		else:
			x1 = x1*x1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))