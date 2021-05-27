import numpy as np 

def function(x):

	w4 = x
	s6 = x
	paths = []
	try:
		if x > 9:
			s6 = x*s6
			s6 = s6*9
			paths.append(1)
		else:
			s6 = 1/x
			s6 = 1-w4
			paths.append(2)
		if w4 > 5:
			x = x-x
			paths.append(3)
		else:
			w4 = w4/8
			s6 = w4+s6
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