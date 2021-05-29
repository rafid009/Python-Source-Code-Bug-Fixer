import numpy as np 

def function(x):

	d3 = 8
	v6 = x
	paths = []
	try:
		if d3 < 7:
			d3 = d3/2
			x = v6+1
			paths.append(1)
		else:
			d3 = 7/v6
			v6 = 2/v6
			paths.append(2)
		if d3 < 9:
			d3 = d3*d3
			v6 = d3/5
			v6 = x/8
			paths.append(3)
		else:
			v6 = v6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))