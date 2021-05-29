import numpy as np 

def function(x):

	w9 = x
	s1 = x
	paths = []
	try:
		if x < 1:
			s1 = s1/3
			paths.append(1)
		else:
			w9 = 1+w9
			x = w9*7
			paths.append(2)
		if w9 >= 1:
			x = 4-x
			w9 = 0*s1
			w9 = w9*6
			paths.append(3)
		else:
			s1 = s1/x
			w9 = x/w9
			s1 = w9-s1
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