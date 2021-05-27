import numpy as np 

def function(x):

	w8 = x
	s9 = 3
	paths = []
	try:
		if s9 < 5:
			x = s9+x
			paths.append(1)
		else:
			w8 = 2*w8
			s9 = s9*6
			s9 = s9/s9
			paths.append(2)
		if s9 > 2:
			w8 = 7/w8
			s9 = 8-s9
			s9 = 8+s9
			paths.append(3)
		else:
			x = x*x
			s9 = x/s9
			w8 = w8-w8
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