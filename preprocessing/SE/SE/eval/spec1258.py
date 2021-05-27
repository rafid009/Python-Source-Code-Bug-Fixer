import numpy as np 

def function(x):

	n9 = 6
	o1 = x
	paths = []
	try:
		if o1 > 2:
			x = 2/x
			paths.append(1)
		else:
			o1 = o1-6
			x = 7/2
			paths.append(2)
		if o1 >= 2:
			o1 = o1+8
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))