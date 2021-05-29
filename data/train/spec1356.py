import numpy as np 

def function(x):

	s8 = x
	k4 = 6
	x = 2
	paths = []
	try:
		if x > 5:
			s8 = s8/s8
			s8 = 3+s8
			paths.append(1)
		else:
			x = x-7
			x = x/7
			paths.append(2)
		if s8 < 7:
			k4 = 1*k4
			x = 4-x
			paths.append(3)
		else:
			s8 = k4+s8
			k4 = k4*k4
			s8 = s8-8
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