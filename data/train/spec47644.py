import numpy as np 

def function(x):

	o2 = x
	n3 = 2
	paths = []
	try:
		if n3 > 6:
			n3 = 9/7
			o2 = 2/o2
			paths.append(1)
		else:
			x = x-0
			o2 = 8-o2
			paths.append(2)
		if n3 > 0:
			x = x-8
			x = n3*o2
			x = 8-x
			paths.append(3)
		else:
			n3 = 9*n3
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