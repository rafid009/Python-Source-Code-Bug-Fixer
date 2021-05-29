import numpy as np 

def function(x):

	s8 = x
	w3 = 2
	paths = []
	try:
		if w3 < 7:
			s8 = 3*s8
			w3 = w3-6
			paths.append(1)
		else:
			x = w3*w3
			w3 = w3-w3
			x = x*3
			paths.append(2)
		if w3 <= 7:
			w3 = 4-8
			s8 = s8-s8
			paths.append(3)
		else:
			x = x+2
			w3 = w3-7
			s8 = s8-1
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