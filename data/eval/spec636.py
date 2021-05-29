import numpy as np 

def function(x):

	x0 = 6
	s5 = x
	paths = []
	try:
		if s5 <= 9:
			x0 = x0-0
			x = x0*x
			paths.append(1)
		else:
			x0 = x0+x
			x = x0*6
			paths.append(2)
		if s5 <= 1:
			x = 3+x
			x = x-2
			x0 = s5/2
			paths.append(3)
		else:
			x = x-4
			s5 = 8+s5
			x0 = x0-s5
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		s5 = x0**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))