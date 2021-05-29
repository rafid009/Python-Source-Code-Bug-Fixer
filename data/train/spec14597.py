import numpy as np 

def function(x):

	r3 = x
	n0 = 7
	paths = []
	try:
		if n0 > 6:
			x = x/n0
			paths.append(1)
		else:
			x = 9/x
			n0 = 1*2
			paths.append(2)
		if x > 6:
			n0 = n0*6
			x = 8+x
			paths.append(3)
		else:
			x = 1-x
			x = x-4
			n0 = n0-x
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