import numpy as np 

def function(x):

	a0 = x
	s1 = x
	paths = []
	try:
		if x < 8:
			s1 = x/2
			s1 = a0-s1
			paths.append(1)
		else:
			s1 = 9+6
			a0 = a0-1
			a0 = a0-1
			paths.append(2)
		if x > 1:
			x = 6-x
			a0 = x-6
			paths.append(3)
		else:
			s1 = 4-s1
			x = 9*a0
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