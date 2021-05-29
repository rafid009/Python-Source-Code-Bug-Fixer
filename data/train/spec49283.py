import numpy as np 

def function(x):

	s0 = x
	d3 = x
	paths = []
	try:
		if d3 >= 4:
			d3 = d3+2
			s0 = 4-6
			d3 = 7-d3
			paths.append(1)
		else:
			s0 = 0+x
			paths.append(2)
		if d3 > 6:
			d3 = 6*d3
			paths.append(3)
		else:
			s0 = 7-s0
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))