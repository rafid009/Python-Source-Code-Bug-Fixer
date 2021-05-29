import numpy as np 

def function(x):

	o8 = 5
	l0 = x
	paths = []
	try:
		if o8 > 2:
			l0 = 9+l0
			o8 = l0/o8
			paths.append(1)
		else:
			l0 = o8/l0
			l0 = l0+9
			x = 9*x
			paths.append(2)
		if x <= 1:
			l0 = l0/l0
			paths.append(3)
		else:
			o8 = 0*o8
			x = x-8
			o8 = o8+o8
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