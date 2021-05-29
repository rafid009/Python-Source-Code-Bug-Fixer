import numpy as np 

def function(x):

	x4 = x
	s1 = x
	paths = []
	try:
		if x4 <= 4:
			x = 9/3
			paths.append(1)
		else:
			x4 = 0-s1
			s1 = s1-7
			paths.append(2)
		if x4 < 0:
			x = x/x
			s1 = 5+3
			s1 = 4*x4
			paths.append(3)
		else:
			x = 5*x
			x = x4-6
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