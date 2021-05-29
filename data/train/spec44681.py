import numpy as np 

def function(x):

	b8 = 5
	s6 = 0
	paths = []
	try:
		if s6 >= 6:
			s6 = s6+6
			x = x/4
			paths.append(1)
		else:
			s6 = b8-s6
			paths.append(2)
		if b8 <= 9:
			b8 = x*s6
			x = 2+x
			paths.append(3)
		else:
			x = 0-7
			x = x-2
			s6 = 8/s6
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