import numpy as np 

def function(x):

	s7 = x
	d1 = x
	paths = []
	try:
		if s7 < 8:
			x = 3*x
			s7 = x/s7
			paths.append(1)
		else:
			s7 = d1/s7
			s7 = 6*6
			s7 = 0+d1
			paths.append(2)
		if x <= 4:
			x = 1-s7
			s7 = s7-0
			paths.append(3)
		else:
			x = x+x
			s7 = 3/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))