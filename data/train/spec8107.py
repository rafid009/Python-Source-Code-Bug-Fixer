import numpy as np 

def function(x):

	p1 = 9
	s0 = x
	paths = []
	try:
		if s0 >= 2:
			x = x/x
			s0 = 6-9
			s0 = s0*2
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if s0 < 9:
			s0 = s0+8
			paths.append(3)
		else:
			x = x+6
			s0 = s0*x
			s0 = s0*s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		p1 = s0**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))