import numpy as np 

def function(x):

	r6 = x
	n6 = x
	paths = []
	try:
		if x > 1:
			x = x*x
			x = 8-n6
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if x > 1:
			n6 = x*n6
			r6 = 7+4
			paths.append(3)
		else:
			n6 = 6-7
			n6 = n6*3
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