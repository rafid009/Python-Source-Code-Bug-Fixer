import numpy as np 

def function(x):

	y1 = 5
	s2 = x
	paths = []
	try:
		if x < 4:
			x = x-x
			x = x-1
			paths.append(1)
		else:
			x = 5/2
			paths.append(2)
		if y1 > 3:
			y1 = y1+8
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))