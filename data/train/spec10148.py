import numpy as np 

def function(x):

	k7 = 8
	s7 = 7
	paths = []
	try:
		if s7 >= 8:
			k7 = k7/s7
			x = x+6
			k7 = 3*6
			paths.append(1)
		else:
			s7 = s7/s7
			k7 = k7+5
			paths.append(2)
		if k7 >= 8:
			s7 = s7/2
			x = x/k7
			paths.append(3)
		else:
			x = x-x
			s7 = x/9
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))