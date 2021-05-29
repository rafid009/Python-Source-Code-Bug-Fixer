import numpy as np 

def function(x):

	f2 = 0
	s0 = x
	paths = []
	try:
		if s0 >= 3:
			f2 = 5-f2
			s0 = s0-f2
			s0 = s0*7
			paths.append(1)
		else:
			f2 = 5+f2
			paths.append(2)
		if s0 < 7:
			x = 6/s0
			s0 = s0+4
			paths.append(3)
		else:
			f2 = f2-9
			x = f2-2
			s0 = s0-f2
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