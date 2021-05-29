import numpy as np 

def function(x):

	x4 = x
	s4 = 7
	paths = []
	try:
		if x >= 7:
			s4 = 7/s4
			x = s4/x4
			paths.append(1)
		else:
			s4 = s4*s4
			x = 6/x4
			paths.append(2)
		if s4 >= 8:
			x4 = x-x4
			s4 = x4*4
			paths.append(3)
		else:
			s4 = 8-9
			x = 3-x
			x4 = 6/8
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