import numpy as np 

def function(x):

	s0 = x
	l3 = 4
	paths = []
	try:
		if l3 > 5:
			l3 = l3-s0
			s0 = s0/s0
			s0 = 6*2
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if s0 <= 1:
			x = x+9
			s0 = l3/s0
			paths.append(3)
		else:
			x = 3*2
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))