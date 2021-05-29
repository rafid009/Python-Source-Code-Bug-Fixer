import numpy as np 

def function(x):

	s4 = 0
	x4 = x
	paths = []
	try:
		if x4 <= 2:
			s4 = s4*x
			paths.append(1)
		else:
			x4 = x4/3
			x4 = 2-7
			x4 = x-9
			paths.append(2)
		if x > 7:
			x4 = x4*7
			paths.append(3)
		else:
			s4 = 9-s4
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