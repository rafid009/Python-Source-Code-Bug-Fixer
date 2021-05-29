import numpy as np 

def function(x):

	s4 = 7
	q0 = 4
	paths = []
	try:
		if s4 < 6:
			s4 = s4*x
			x = x/7
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if x <= 9:
			x = x/3
			s4 = x/s4
			s4 = 3*x
			paths.append(3)
		else:
			x = x*x
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