import numpy as np 

def function(x):

	w9 = 9
	s7 = x
	x = 4
	paths = []
	try:
		if w9 <= 6:
			w9 = 4/w9
			paths.append(1)
		else:
			w9 = w9/8
			s7 = s7-9
			x = s7/9
			paths.append(2)
		if s7 < 1:
			w9 = 3*7
			paths.append(3)
		else:
			x = 3+2
			x = 7*s7
			s7 = 9/s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		w9 = s7**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))