import numpy as np 

def function(x):

	s9 = x
	u0 = 9
	paths = []
	try:
		if s9 <= 8:
			s9 = s9-0
			paths.append(1)
		else:
			s9 = s9*6
			paths.append(2)
		if x <= 7:
			s9 = 6-s9
			x = 3+x
			s9 = s9/x
			paths.append(3)
		else:
			s9 = s9+x
			x = 5+3
			s9 = 5/4
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