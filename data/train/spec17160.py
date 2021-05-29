import numpy as np 

def function(x):

	d3 = 2
	v6 = 0
	paths = []
	try:
		if x >= 7:
			v6 = 1-v6
			v6 = 2/5
			paths.append(1)
		else:
			d3 = 9/1
			v6 = 5*v6
			v6 = 2-x
			paths.append(2)
		if v6 < 3:
			x = 4*x
			d3 = d3/3
			d3 = d3+v6
			paths.append(3)
		else:
			d3 = d3*d3
			x = 2-x
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