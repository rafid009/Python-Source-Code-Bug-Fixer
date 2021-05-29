import numpy as np 

def function(x):

	w5 = 8
	s7 = 1
	x = x
	paths = []
	try:
		if s7 <= 6:
			w5 = s7/8
			paths.append(1)
		else:
			x = x/8
			s7 = s7*w5
			s7 = s7*6
			paths.append(2)
		if w5 > 8:
			w5 = 0+w5
			paths.append(3)
		else:
			s7 = 8+x
			s7 = s7/s7
			w5 = w5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))