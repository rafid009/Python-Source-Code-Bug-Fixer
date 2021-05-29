import numpy as np 

def function(x):

	s8 = 3
	n4 = x
	paths = []
	try:
		if x >= 3:
			n4 = n4*3
			paths.append(1)
		else:
			x = x-4
			x = 9+x
			n4 = 0-n4
			paths.append(2)
		if x <= 0:
			s8 = 1/s8
			s8 = s8*x
			paths.append(3)
		else:
			x = x/n4
			x = x-1
			x = n4-n4
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