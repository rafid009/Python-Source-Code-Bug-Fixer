import numpy as np 

def function(x):

	v6 = x
	d3 = x
	paths = []
	try:
		if x > 2:
			x = 4/2
			x = 4*0
			v6 = 3*v6
			paths.append(1)
		else:
			v6 = 8/7
			d3 = 8*d3
			v6 = 0+v6
			paths.append(2)
		if x >= 8:
			d3 = d3-x
			v6 = v6/4
			x = x-7
			paths.append(3)
		else:
			v6 = 6/v6
			d3 = d3+v6
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