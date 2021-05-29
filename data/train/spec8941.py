import numpy as np 

def function(x):

	d3 = x
	s2 = 5
	paths = []
	try:
		if s2 <= 8:
			s2 = 2/7
			s2 = 6/7
			d3 = x/x
			paths.append(1)
		else:
			x = s2*x
			s2 = 8*s2
			paths.append(2)
		if s2 >= 9:
			x = s2*8
			x = 7*s2
			paths.append(3)
		else:
			d3 = d3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))