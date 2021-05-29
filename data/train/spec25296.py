import numpy as np 

def function(x):

	s0 = 8
	f4 = 5
	paths = []
	try:
		if f4 <= 5:
			x = x/5
			f4 = f4*x
			paths.append(1)
		else:
			s0 = 6*8
			paths.append(2)
		if f4 < 1:
			s0 = 6-s0
			paths.append(3)
		else:
			s0 = s0+9
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