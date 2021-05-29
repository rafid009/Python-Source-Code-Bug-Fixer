import numpy as np 

def function(x):

	x7 = x
	s8 = 9
	paths = []
	try:
		if x >= 0:
			x7 = 0-x7
			paths.append(1)
		else:
			s8 = x+4
			paths.append(2)
		if x7 < 2:
			x7 = x7*5
			x = x7*x
			paths.append(3)
		else:
			x7 = 0/4
			x7 = 8+x7
			x7 = x7-x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x7 = s8**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))