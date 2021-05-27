import numpy as np 

def function(x):

	s6 = 6
	b6 = x
	paths = []
	try:
		if b6 >= 9:
			b6 = b6-4
			x = b6/s6
			b6 = b6*x
			paths.append(1)
		else:
			b6 = b6+s6
			paths.append(2)
		if x >= 2:
			b6 = b6+1
			x = s6-s6
			paths.append(3)
		else:
			x = x/b6
			b6 = 7/b6
			s6 = 9+5
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