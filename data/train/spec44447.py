import numpy as np 

def function(x):

	s6 = 1
	n5 = 6
	paths = []
	try:
		if s6 > 6:
			n5 = 6*x
			paths.append(1)
		else:
			n5 = 2/3
			paths.append(2)
		if s6 < 6:
			x = n5*x
			n5 = 1+s6
			n5 = n5*x
			paths.append(3)
		else:
			n5 = 5/n5
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