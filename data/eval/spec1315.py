import numpy as np 

def function(x):

	y1 = x
	s4 = x
	paths = []
	try:
		if x < 8:
			s4 = s4/5
			paths.append(1)
		else:
			x = s4-y1
			y1 = 9-y1
			y1 = y1/y1
			paths.append(2)
		if x >= 8:
			s4 = s4*y1
			paths.append(3)
		else:
			s4 = s4-y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))