import numpy as np 

def function(x):

	w8 = x
	s7 = x
	paths = []
	try:
		if x >= 6:
			w8 = 3+w8
			s7 = s7*w8
			s7 = 0/x
			paths.append(1)
		else:
			s7 = x+1
			paths.append(2)
		if w8 > 3:
			w8 = 5+w8
			w8 = 3-3
			s7 = w8+6
			paths.append(3)
		else:
			w8 = w8+w8
			w8 = 0-w8
			x = w8/s7
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