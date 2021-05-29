import numpy as np 

def function(x):

	x7 = x
	s7 = 5
	paths = []
	try:
		if x7 < 1:
			x7 = 4/9
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if s7 >= 9:
			x = x+6
			paths.append(3)
		else:
			x7 = x7-7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))