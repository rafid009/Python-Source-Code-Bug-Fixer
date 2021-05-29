import numpy as np 

def function(x):

	s9 = x
	d3 = x
	paths = []
	try:
		if s9 <= 9:
			s9 = s9-4
			paths.append(1)
		else:
			d3 = d3/4
			paths.append(2)
		if s9 <= 3:
			d3 = s9+d3
			paths.append(3)
		else:
			x = x*s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))