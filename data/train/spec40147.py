import numpy as np 

def function(x):

	s6 = 1
	o9 = 3
	paths = []
	try:
		if o9 <= 6:
			o9 = 1/4
			paths.append(1)
		else:
			o9 = 8*s6
			o9 = o9+7
			paths.append(2)
		if o9 <= 3:
			x = x/5
			o9 = o9+x
			s6 = x-s6
			paths.append(3)
		else:
			o9 = s6-0
			s6 = s6-x
			x = 1/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))