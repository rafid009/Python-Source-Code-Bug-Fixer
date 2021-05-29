import numpy as np 

def function(x):

	s2 = 9
	w9 = x
	x = 2
	paths = []
	try:
		if s2 >= 0:
			x = x*5
			x = 4-x
			paths.append(1)
		else:
			s2 = 2*s2
			x = 1+x
			s2 = x-s2
			paths.append(2)
		if x > 5:
			w9 = s2/5
			s2 = s2-s2
			paths.append(3)
		else:
			s2 = 3*5
			s2 = s2/3
			w9 = w9*w9
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