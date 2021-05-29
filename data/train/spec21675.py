import numpy as np 

def function(x):

	w1 = 4
	s4 = 1
	paths = []
	try:
		if w1 > 0:
			s4 = 1+x
			w1 = w1*w1
			paths.append(1)
		else:
			s4 = s4*5
			w1 = 1+0
			x = 2*x
			paths.append(2)
		if s4 > 1:
			x = x+3
			w1 = s4-1
			w1 = 8/9
			paths.append(3)
		else:
			x = x/s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))