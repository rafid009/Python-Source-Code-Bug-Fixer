import numpy as np 

def function(x):

	o8 = 2
	s4 = x
	paths = []
	try:
		if s4 < 0:
			s4 = 0-s4
			paths.append(1)
		else:
			x = 3/4
			x = 3+0
			s4 = s4/s4
			paths.append(2)
		if s4 >= 1:
			s4 = x*1
			paths.append(3)
		else:
			x = 5/x
			x = 2/o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))