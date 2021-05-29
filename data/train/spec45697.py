import numpy as np 

def function(x):

	s0 = 3
	l4 = 4
	paths = []
	try:
		if x < 6:
			x = 5*x
			paths.append(1)
		else:
			x = 9-x
			s0 = s0*l4
			l4 = 6/l4
			paths.append(2)
		if l4 > 8:
			s0 = 7-2
			paths.append(3)
		else:
			x = 6/x
			l4 = 5+8
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