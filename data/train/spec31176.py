import numpy as np 

def function(x):

	s9 = x
	y8 = x
	paths = []
	try:
		if y8 < 0:
			y8 = y8-1
			y8 = 7-s9
			y8 = 0-y8
			paths.append(1)
		else:
			x = 5+x
			y8 = 5*y8
			s9 = s9+6
			paths.append(2)
		if y8 < 2:
			x = s9*x
			x = x*x
			paths.append(3)
		else:
			y8 = y8-y8
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		y8 = s9**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))