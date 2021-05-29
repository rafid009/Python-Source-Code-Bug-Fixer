import numpy as np 

def function(x):

	n2 = x
	s0 = 7
	paths = []
	try:
		if x < 3:
			n2 = 3*n2
			paths.append(1)
		else:
			s0 = s0/s0
			n2 = n2+4
			n2 = 1*n2
			paths.append(2)
		if x <= 6:
			x = 2-x
			paths.append(3)
		else:
			s0 = 7*s0
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