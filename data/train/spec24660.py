import numpy as np 

def function(x):

	s0 = 4
	d5 = x
	x = 3
	paths = []
	try:
		if s0 < 2:
			x = 0+x
			paths.append(1)
		else:
			x = x*4
			s0 = 2*s0
			paths.append(2)
		if s0 >= 6:
			s0 = 6*s0
			x = 4-x
			d5 = d5/5
			paths.append(3)
		else:
			s0 = 4+x
			s0 = 1/8
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))