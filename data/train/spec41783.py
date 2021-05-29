import numpy as np 

def function(x):

	s0 = x
	f8 = 1
	x = 6
	paths = []
	try:
		if x > 0:
			x = 2/x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if f8 <= 4:
			x = x+s0
			paths.append(3)
		else:
			f8 = 2*f8
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