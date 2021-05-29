import numpy as np 

def function(x):

	s0 = x
	o1 = x
	x = 8
	paths = []
	try:
		if s0 >= 9:
			s0 = x-8
			x = 5*2
			s0 = 3-s0
			paths.append(1)
		else:
			s0 = 0+1
			x = 0-7
			o1 = 8-x
			paths.append(2)
		if s0 >= 2:
			o1 = 8-o1
			paths.append(3)
		else:
			o1 = o1/6
			s0 = s0-o1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		s0 = o1**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))