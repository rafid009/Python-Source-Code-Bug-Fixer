import numpy as np 

def function(x):

	s7 = 5
	d4 = 6
	paths = []
	try:
		if d4 >= 0:
			s7 = 9/s7
			d4 = d4*9
			s7 = 7+3
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if s7 > 1:
			d4 = 7+8
			paths.append(3)
		else:
			d4 = d4-0
			s7 = 0-s7
			s7 = s7*s7
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