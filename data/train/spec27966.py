import numpy as np 

def function(x):

	f3 = 3
	n1 = 3
	paths = []
	try:
		if f3 <= 9:
			n1 = 6*n1
			x = x*f3
			paths.append(1)
		else:
			x = x*n1
			n1 = 9/7
			n1 = 0*f3
			paths.append(2)
		if f3 < 0:
			n1 = 9*6
			n1 = 4+8
			n1 = n1+8
			paths.append(3)
		else:
			f3 = 8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))