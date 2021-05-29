import numpy as np 

def function(x):

	s7 = 7
	f3 = 2
	paths = []
	try:
		if s7 >= 3:
			f3 = f3+4
			paths.append(1)
		else:
			s7 = 9+9
			paths.append(2)
		if s7 > 3:
			s7 = x-s7
			paths.append(3)
		else:
			s7 = s7-8
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