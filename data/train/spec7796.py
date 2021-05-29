import numpy as np 

def function(x):

	o1 = x
	n0 = 1
	paths = []
	try:
		if o1 >= 6:
			o1 = o1+5
			x = 1*5
			x = 2/x
			paths.append(1)
		else:
			o1 = 1+o1
			n0 = 2+n0
			paths.append(2)
		if n0 > 4:
			x = 6*x
			o1 = o1*6
			o1 = o1*o1
			paths.append(3)
		else:
			x = 9/x
			o1 = o1/x
			x = 1-4
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