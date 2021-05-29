import numpy as np 

def function(x):

	n7 = x
	s0 = 8
	paths = []
	try:
		if x < 8:
			x = x-3
			paths.append(1)
		else:
			s0 = 4*4
			n7 = x-5
			paths.append(2)
		if s0 > 8:
			s0 = 3*8
			s0 = 5-s0
			paths.append(3)
		else:
			n7 = 0+x
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