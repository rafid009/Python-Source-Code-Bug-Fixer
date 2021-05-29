import numpy as np 

def function(x):

	d3 = 8
	s2 = 8
	paths = []
	try:
		if x > 4:
			x = 0+x
			x = 6/x
			paths.append(1)
		else:
			s2 = s2+s2
			x = x-3
			d3 = d3/s2
			paths.append(2)
		if s2 >= 7:
			d3 = 4-d3
			x = x*8
			d3 = d3-9
			paths.append(3)
		else:
			x = s2/9
			d3 = d3/d3
			d3 = d3/d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))