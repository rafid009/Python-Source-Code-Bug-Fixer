import numpy as np 

def function(x):

	n0 = x
	o1 = 8
	paths = []
	try:
		if x >= 4:
			x = x-4
			n0 = n0+8
			paths.append(1)
		else:
			x = 7+n0
			x = 7-o1
			paths.append(2)
		if o1 >= 6:
			n0 = 0/o1
			n0 = 4/o1
			paths.append(3)
		else:
			x = x+o1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))