import numpy as np 

def function(x):

	s4 = x
	o8 = x
	paths = []
	try:
		if x <= 3:
			o8 = o8/s4
			x = 0*x
			paths.append(1)
		else:
			s4 = 7*s4
			x = 6-o8
			paths.append(2)
		if s4 < 4:
			x = 5/s4
			x = 3*x
			s4 = s4-0
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))