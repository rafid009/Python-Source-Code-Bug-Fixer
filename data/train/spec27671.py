import numpy as np 

def function(x):

	w4 = x
	s5 = 9
	paths = []
	try:
		if w4 >= 7:
			w4 = w4-5
			w4 = 1/s5
			s5 = s5+9
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if s5 <= 4:
			s5 = s5-8
			x = s5*w4
			w4 = 1-w4
			paths.append(3)
		else:
			s5 = 7-s5
			w4 = 7/6
			x = x-w4
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