import numpy as np 

def function(x):

	w1 = x
	s8 = x
	paths = []
	try:
		if x < 1:
			s8 = s8-2
			paths.append(1)
		else:
			w1 = s8*s8
			paths.append(2)
		if s8 <= 2:
			x = x+8
			x = x-5
			paths.append(3)
		else:
			s8 = 9-w1
			w1 = w1+s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))