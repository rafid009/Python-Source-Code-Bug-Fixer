import numpy as np 

def function(x):

	a9 = 5
	s0 = 6
	paths = []
	try:
		if s0 < 8:
			a9 = 8/a9
			a9 = x-2
			s0 = 1-s0
			paths.append(1)
		else:
			a9 = x/a9
			paths.append(2)
		if x <= 4:
			a9 = a9*5
			paths.append(3)
		else:
			s0 = s0+a9
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