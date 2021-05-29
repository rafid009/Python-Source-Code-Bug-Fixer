import numpy as np 

def function(x):

	d2 = x
	s0 = x
	paths = []
	try:
		if x >= 7:
			x = 4*x
			x = 0-3
			paths.append(1)
		else:
			s0 = s0*d2
			x = 6+x
			paths.append(2)
		if d2 <= 1:
			d2 = 6/d2
			s0 = 9*s0
			s0 = s0*x
			paths.append(3)
		else:
			s0 = s0/d2
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))