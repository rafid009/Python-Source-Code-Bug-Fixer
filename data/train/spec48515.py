import numpy as np 

def function(x):

	s8 = x
	l8 = 9
	paths = []
	try:
		if s8 < 3:
			x = x+7
			s8 = s8-7
			l8 = 7/2
			paths.append(1)
		else:
			l8 = 3*l8
			l8 = l8*l8
			s8 = s8-x
			paths.append(2)
		if s8 <= 3:
			s8 = l8*1
			x = 2*x
			l8 = l8/7
			paths.append(3)
		else:
			x = 2*x
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