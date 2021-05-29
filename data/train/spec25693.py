import numpy as np 

def function(x):

	r6 = x
	s0 = 4
	paths = []
	try:
		if x <= 7:
			s0 = 6+7
			paths.append(1)
		else:
			r6 = 8/9
			paths.append(2)
		if s0 < 8:
			x = x-2
			r6 = 5-r6
			paths.append(3)
		else:
			r6 = 8/r6
			r6 = r6*6
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