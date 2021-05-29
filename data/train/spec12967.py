import numpy as np 

def function(x):

	n1 = x
	r1 = 8
	paths = []
	try:
		if r1 < 3:
			n1 = 3-n1
			paths.append(1)
		else:
			n1 = 8*n1
			r1 = 3/r1
			n1 = n1*x
			paths.append(2)
		if x >= 3:
			n1 = 3*3
			paths.append(3)
		else:
			n1 = n1+n1
			n1 = 6+3
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