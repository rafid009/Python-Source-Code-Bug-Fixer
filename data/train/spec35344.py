import numpy as np 

def function(x):

	s0 = x
	o8 = 3
	paths = []
	try:
		if s0 < 0:
			o8 = x-9
			s0 = s0+1
			paths.append(1)
		else:
			s0 = s0*o8
			paths.append(2)
		if s0 < 3:
			x = 9/6
			x = o8*2
			x = s0+x
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))