import numpy as np 

def function(x):

	d3 = 6
	s9 = x
	x = 5
	paths = []
	try:
		if s9 < 6:
			d3 = d3/d3
			paths.append(1)
		else:
			x = x*d3
			paths.append(2)
		if s9 > 1:
			s9 = s9*3
			s9 = s9-d3
			paths.append(3)
		else:
			d3 = 3+d3
			x = 6*x
			x = x/d3
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))