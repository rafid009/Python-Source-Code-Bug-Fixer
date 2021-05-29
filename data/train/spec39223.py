import numpy as np 

def function(x):

	s4 = 1
	x0 = x
	paths = []
	try:
		if x >= 3:
			x0 = x-s4
			paths.append(1)
		else:
			s4 = x0/x
			paths.append(2)
		if s4 > 2:
			s4 = 0-6
			x0 = x0*3
			s4 = s4-s4
			paths.append(3)
		else:
			x0 = 8/x0
			x = 6-2
			s4 = 9-s4
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))