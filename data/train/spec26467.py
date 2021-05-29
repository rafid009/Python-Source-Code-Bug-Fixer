import numpy as np 

def function(x):

	z2 = x
	s7 = 7
	paths = []
	try:
		if z2 <= 8:
			x = 3+x
			paths.append(1)
		else:
			x = x-s7
			s7 = s7+0
			paths.append(2)
		if s7 > 3:
			s7 = 2*5
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))