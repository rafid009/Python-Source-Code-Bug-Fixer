import numpy as np 

def function(x):

	s0 = x
	w4 = 1
	paths = []
	try:
		if s0 >= 5:
			w4 = x+s0
			paths.append(1)
		else:
			x = x+4
			x = x*s0
			paths.append(2)
		if w4 >= 2:
			s0 = s0-1
			x = 7+x
			paths.append(3)
		else:
			x = s0+x
			w4 = 4*x
			s0 = 2+s0
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