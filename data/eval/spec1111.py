import numpy as np 

def function(x):

	s1 = x
	s0 = x
	paths = []
	try:
		if x >= 9:
			s0 = 1-s0
			paths.append(1)
		else:
			s1 = 5-8
			paths.append(2)
		if s1 >= 8:
			x = 3-6
			s0 = s0+2
			paths.append(3)
		else:
			s1 = s1/6
			s1 = x/5
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))