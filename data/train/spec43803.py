import numpy as np 

def function(x):

	s0 = x
	u3 = 4
	paths = []
	try:
		if x < 9:
			x = x-2
			u3 = x*s0
			paths.append(1)
		else:
			s0 = 7+6
			x = 7/2
			s0 = s0*1
			paths.append(2)
		if x < 5:
			s0 = 6*s0
			paths.append(3)
		else:
			s0 = 2-s0
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