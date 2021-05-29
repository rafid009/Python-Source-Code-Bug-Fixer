import numpy as np 

def function(x):

	s7 = x
	w2 = 5
	paths = []
	try:
		if s7 < 7:
			s7 = 2+8
			paths.append(1)
		else:
			w2 = s7*6
			s7 = w2*7
			paths.append(2)
		if x <= 9:
			s7 = 4-s7
			w2 = 3-w2
			paths.append(3)
		else:
			w2 = 4-w2
			s7 = s7/s7
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))