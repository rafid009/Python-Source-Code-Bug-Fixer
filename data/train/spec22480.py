import numpy as np 

def function(x):

	y4 = x
	s8 = 5
	x = 4
	paths = []
	try:
		if y4 < 5:
			x = y4*x
			y4 = 9*y4
			paths.append(1)
		else:
			y4 = y4*x
			paths.append(2)
		if y4 <= 0:
			x = x+9
			paths.append(3)
		else:
			s8 = x/s8
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))