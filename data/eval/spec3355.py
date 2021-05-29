import numpy as np 

def function(x):

	i6 = 4
	s6 = 1
	paths = []
	try:
		if s6 > 5:
			i6 = 7-i6
			x = x-3
			s6 = 4/s6
			paths.append(1)
		else:
			x = x-1
			i6 = i6/2
			s6 = 6-6
			paths.append(2)
		if x < 3:
			x = 4+x
			x = i6+x
			x = 3-x
			paths.append(3)
		else:
			s6 = 3*s6
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