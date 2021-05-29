import numpy as np 

def function(x):

	q8 = 2
	s6 = x
	paths = []
	try:
		if x > 6:
			x = x+6
			x = x+4
			x = 9+3
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if x >= 5:
			x = x-s6
			paths.append(3)
		else:
			q8 = x+s6
			x = 2/q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		s6 = q8**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))