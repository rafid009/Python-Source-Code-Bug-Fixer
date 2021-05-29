import numpy as np 

def function(x):

	s1 = 8
	w4 = x
	paths = []
	try:
		if x <= 1:
			x = x+1
			paths.append(1)
		else:
			w4 = 3/s1
			paths.append(2)
		if w4 <= 1:
			s1 = w4*s1
			x = 1*x
			s1 = 9-s1
			paths.append(3)
		else:
			w4 = w4+8
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