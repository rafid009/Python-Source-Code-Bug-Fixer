import numpy as np 

def function(x):

	s0 = x
	o4 = 7
	paths = []
	try:
		if o4 >= 1:
			x = x*6
			o4 = 8/x
			x = o4/o4
			paths.append(1)
		else:
			s0 = s0-4
			x = 4+x
			x = x*6
			paths.append(2)
		if o4 >= 2:
			x = x-s0
			paths.append(3)
		else:
			o4 = o4*5
			o4 = o4*4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		s0 = o4**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))