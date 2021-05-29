import numpy as np 

def function(x):

	b9 = 6
	s6 = 0
	paths = []
	try:
		if x < 7:
			x = x+2
			b9 = 7*s6
			b9 = 7*8
			paths.append(1)
		else:
			b9 = b9*b9
			s6 = 9+s6
			x = 2*x
			paths.append(2)
		if x < 1:
			b9 = b9/4
			b9 = x-b9
			b9 = s6+x
			paths.append(3)
		else:
			b9 = 4/x
			x = 5-s6
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