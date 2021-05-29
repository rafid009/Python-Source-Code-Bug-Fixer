import numpy as np 

def function(x):

	w4 = x
	s7 = 4
	paths = []
	try:
		if w4 >= 3:
			w4 = w4-6
			s7 = s7-w4
			x = x-4
			paths.append(1)
		else:
			s7 = s7+w4
			x = w4/7
			s7 = w4*2
			paths.append(2)
		if s7 < 0:
			x = x/w4
			paths.append(3)
		else:
			s7 = s7-s7
			s7 = 8*s7
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))