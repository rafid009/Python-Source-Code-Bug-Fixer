import numpy as np 

def function(x):

	n3 = 4
	s0 = 5
	paths = []
	try:
		if x > 1:
			x = x*0
			paths.append(1)
		else:
			s0 = s0+8
			s0 = s0/x
			n3 = 3+x
			paths.append(2)
		if s0 >= 0:
			s0 = s0*3
			s0 = s0-4
			paths.append(3)
		else:
			s0 = s0*8
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		s0 = n3**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))