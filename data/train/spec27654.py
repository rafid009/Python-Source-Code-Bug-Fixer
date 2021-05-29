import numpy as np 

def function(x):

	a0 = 8
	s8 = x
	paths = []
	try:
		if a0 <= 9:
			x = 2/x
			paths.append(1)
		else:
			a0 = a0*s8
			paths.append(2)
		if x > 3:
			s8 = s8+3
			s8 = 4-s8
			paths.append(3)
		else:
			a0 = a0+x
			x = x+5
			x = 2-x
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