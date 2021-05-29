import numpy as np 

def function(x):

	s0 = 2
	x2 = 2
	paths = []
	try:
		if x > 7:
			x = 6*x
			x = 1-3
			x = x+7
			paths.append(1)
		else:
			x2 = x2-6
			paths.append(2)
		if s0 <= 0:
			s0 = 2+6
			paths.append(3)
		else:
			x = 6*s0
			x2 = 3*x2
			s0 = 5*s0
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))