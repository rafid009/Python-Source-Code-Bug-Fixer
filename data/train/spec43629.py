import numpy as np 

def function(x):

	s0 = 0
	f5 = 0
	paths = []
	try:
		if f5 > 0:
			f5 = x*f5
			paths.append(1)
		else:
			f5 = f5-8
			f5 = x-f5
			s0 = s0-0
			paths.append(2)
		if f5 > 5:
			x = 4*x
			paths.append(3)
		else:
			x = 6/x
			s0 = s0/f5
			s0 = x+2
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