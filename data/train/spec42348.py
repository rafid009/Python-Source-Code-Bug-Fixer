import numpy as np 

def function(x):

	k4 = x
	s1 = 0
	paths = []
	try:
		if x > 4:
			s1 = s1-s1
			k4 = k4-0
			x = 6+x
			paths.append(1)
		else:
			k4 = 0*k4
			paths.append(2)
		if s1 > 8:
			s1 = s1/s1
			k4 = x/8
			paths.append(3)
		else:
			k4 = 6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))