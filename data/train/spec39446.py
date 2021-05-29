import numpy as np 

def function(x):

	b7 = 1
	s0 = x
	paths = []
	try:
		if s0 < 8:
			x = x-6
			paths.append(1)
		else:
			x = 3-0
			paths.append(2)
		if x <= 2:
			s0 = 8-s0
			b7 = 6*b7
			paths.append(3)
		else:
			s0 = 9+s0
			x = x+x
			s0 = b7*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))