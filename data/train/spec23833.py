import numpy as np 

def function(x):

	s0 = x
	l1 = 0
	paths = []
	try:
		if s0 < 8:
			x = x-5
			x = x-x
			l1 = l1-x
			paths.append(1)
		else:
			s0 = 0/1
			x = x+x
			paths.append(2)
		if l1 >= 2:
			s0 = l1/7
			l1 = 5/l1
			paths.append(3)
		else:
			l1 = s0*l1
			x = l1-x
			l1 = 9-l1
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