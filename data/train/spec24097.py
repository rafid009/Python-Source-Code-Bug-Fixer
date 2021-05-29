import numpy as np 

def function(x):

	s0 = x
	o5 = 3
	paths = []
	try:
		if x > 0:
			s0 = s0+6
			s0 = 6*5
			s0 = s0-s0
			paths.append(1)
		else:
			s0 = s0-7
			o5 = o5-s0
			o5 = o5-6
			paths.append(2)
		if x < 5:
			s0 = 3/3
			s0 = 0/s0
			paths.append(3)
		else:
			s0 = s0+s0
			o5 = 2*o5
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