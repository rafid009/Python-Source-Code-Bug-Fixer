import numpy as np 

def function(x):

	w1 = x
	s0 = 4
	paths = []
	try:
		if w1 <= 3:
			w1 = 2*x
			paths.append(1)
		else:
			s0 = x-x
			x = 1*x
			w1 = w1-s0
			paths.append(2)
		if s0 < 3:
			s0 = 5-s0
			s0 = s0-7
			paths.append(3)
		else:
			x = w1/5
			s0 = w1*w1
			x = x-7
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))