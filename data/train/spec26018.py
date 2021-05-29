import numpy as np 

def function(x):

	s7 = 2
	w9 = x
	paths = []
	try:
		if s7 >= 2:
			s7 = s7/s7
			s7 = s7-6
			paths.append(1)
		else:
			w9 = 0/9
			paths.append(2)
		if x > 7:
			w9 = w9/9
			w9 = 8*w9
			paths.append(3)
		else:
			w9 = 7/x
			s7 = s7-0
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