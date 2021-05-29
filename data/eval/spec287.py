import numpy as np 

def function(x):

	u2 = 0
	s7 = x
	paths = []
	try:
		if x >= 2:
			u2 = 4-x
			paths.append(1)
		else:
			s7 = s7*s7
			paths.append(2)
		if x >= 2:
			u2 = 8+u2
			paths.append(3)
		else:
			s7 = 9+x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))