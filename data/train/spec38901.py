import numpy as np 

def function(x):

	o8 = 9
	s6 = x
	paths = []
	try:
		if s6 <= 1:
			s6 = x-s6
			o8 = 8*6
			paths.append(1)
		else:
			o8 = 0+o8
			paths.append(2)
		if s6 <= 4:
			s6 = 5+s6
			s6 = s6*6
			o8 = 3-4
			paths.append(3)
		else:
			s6 = 1*s6
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