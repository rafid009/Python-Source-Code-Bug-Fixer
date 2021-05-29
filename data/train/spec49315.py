import numpy as np 

def function(x):

	s0 = x
	f7 = 5
	paths = []
	try:
		if f7 > 8:
			s0 = s0/1
			paths.append(1)
		else:
			f7 = f7-1
			paths.append(2)
		if f7 <= 3:
			f7 = 6-s0
			paths.append(3)
		else:
			x = 8/s0
			f7 = 8-1
			s0 = s0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))