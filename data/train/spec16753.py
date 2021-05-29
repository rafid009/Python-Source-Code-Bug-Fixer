import numpy as np 

def function(x):

	s6 = 6
	x5 = x
	paths = []
	try:
		if x5 < 3:
			x5 = s6*s6
			paths.append(1)
		else:
			x = 3+3
			x = x-x
			x = x5-6
			paths.append(2)
		if x5 > 7:
			s6 = 7/2
			x = x-6
			x = x+x
			paths.append(3)
		else:
			s6 = x5-x
			x = x+3
			s6 = x5+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))