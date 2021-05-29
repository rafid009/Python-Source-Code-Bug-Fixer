import numpy as np 

def function(x):

	y1 = x
	s1 = x
	paths = []
	try:
		if x >= 4:
			x = x/x
			paths.append(1)
		else:
			x = 1/2
			paths.append(2)
		if s1 >= 0:
			s1 = 7-s1
			s1 = 4/y1
			x = 3-x
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))