import numpy as np 

def function(x):

	d3 = 2
	s5 = x
	paths = []
	try:
		if d3 >= 0:
			d3 = d3-0
			x = 6/x
			d3 = 4*x
			paths.append(1)
		else:
			d3 = x*x
			d3 = s5*7
			s5 = s5*6
			paths.append(2)
		if x >= 4:
			d3 = 8*7
			s5 = s5-d3
			x = 8/x
			paths.append(3)
		else:
			s5 = 1+s5
			s5 = s5+5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		d3 = s5**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))