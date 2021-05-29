import numpy as np 

def function(x):

	s6 = x
	y2 = 3
	x = x
	paths = []
	try:
		if x >= 2:
			s6 = s6+x
			s6 = y2+8
			y2 = 2*s6
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x > 4:
			y2 = s6+8
			x = x-9
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))