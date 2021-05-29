import numpy as np 

def function(x):

	s0 = x
	a6 = x
	paths = []
	try:
		if x > 8:
			a6 = a6-6
			a6 = 6-a6
			s0 = x/s0
			paths.append(1)
		else:
			a6 = 9/2
			paths.append(2)
		if s0 > 4:
			x = 9*x
			paths.append(3)
		else:
			a6 = a6*s0
			s0 = 3/s0
			x = s0*5
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))