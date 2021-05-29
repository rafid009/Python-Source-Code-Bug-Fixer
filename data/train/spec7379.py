import numpy as np 

def function(x):

	s6 = 9
	d3 = 7
	paths = []
	try:
		if x < 3:
			d3 = d3/2
			x = x-9
			paths.append(1)
		else:
			d3 = d3/x
			d3 = d3*7
			d3 = s6+d3
			paths.append(2)
		if s6 > 8:
			s6 = 3/s6
			d3 = d3-x
			d3 = s6-9
			paths.append(3)
		else:
			x = x*0
			x = x+6
			x = x-1
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