import numpy as np 

def function(x):

	o1 = x
	l4 = 1
	paths = []
	try:
		if o1 < 8:
			l4 = 2+0
			paths.append(1)
		else:
			o1 = 6+o1
			paths.append(2)
		if o1 >= 1:
			l4 = 6*l4
			paths.append(3)
		else:
			x = x-7
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