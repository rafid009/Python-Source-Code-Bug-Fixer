import numpy as np 

def function(x):

	y6 = x
	s0 = 7
	paths = []
	try:
		if x >= 7:
			x = x-9
			paths.append(1)
		else:
			y6 = y6+9
			s0 = 1*7
			paths.append(2)
		if s0 >= 3:
			s0 = 4/x
			paths.append(3)
		else:
			y6 = 4-5
			s0 = 0/s0
			s0 = 1+s0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))