import numpy as np 

def function(x):

	a0 = 1
	s9 = x
	paths = []
	try:
		if a0 >= 6:
			a0 = a0-7
			s9 = 9-3
			paths.append(1)
		else:
			a0 = a0/2
			x = 1-x
			a0 = a0*x
			paths.append(2)
		if s9 < 0:
			x = 5*x
			paths.append(3)
		else:
			a0 = a0/a0
			x = a0/x
			x = 2-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))