import numpy as np 

def function(x):

	x9 = 7
	s7 = x
	x = x
	paths = []
	try:
		if x >= 4:
			x = s7-7
			paths.append(1)
		else:
			x9 = 5-x9
			paths.append(2)
		if x9 > 6:
			s7 = x9*4
			x = 0-x
			paths.append(3)
		else:
			s7 = 9+9
			s7 = s7-x
			s7 = s7+x9
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