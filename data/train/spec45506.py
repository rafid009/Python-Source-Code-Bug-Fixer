import numpy as np 

def function(x):

	d3 = 4
	s8 = 0
	paths = []
	try:
		if x < 1:
			d3 = 3*9
			x = 8+5
			paths.append(1)
		else:
			s8 = 9+6
			d3 = d3-9
			s8 = 5+1
			paths.append(2)
		if s8 >= 9:
			x = x*x
			d3 = d3+0
			paths.append(3)
		else:
			s8 = x-s8
			x = x*7
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		s8 = d3**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))