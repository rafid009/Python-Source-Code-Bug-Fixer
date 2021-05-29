import numpy as np 

def function(x):

	s0 = x
	d3 = x
	x = x
	paths = []
	try:
		if s0 <= 0:
			s0 = s0-6
			paths.append(1)
		else:
			d3 = d3-1
			paths.append(2)
		if x > 4:
			d3 = d3-d3
			x = x+5
			paths.append(3)
		else:
			d3 = 4*4
			d3 = 2*d3
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