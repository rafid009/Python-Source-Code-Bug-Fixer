import numpy as np 

def function(x):

	s4 = 7
	d3 = 6
	paths = []
	try:
		if s4 <= 0:
			s4 = s4-7
			d3 = 1+5
			x = s4*2
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if s4 >= 8:
			d3 = 6/1
			paths.append(3)
		else:
			d3 = d3-7
			x = x+x
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