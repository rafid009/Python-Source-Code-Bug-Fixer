import numpy as np 

def function(x):

	n7 = x
	d3 = x
	paths = []
	try:
		if x <= 9:
			x = 8*1
			x = x/x
			x = 0*d3
			paths.append(1)
		else:
			x = x*7
			d3 = x-d3
			d3 = 2-d3
			paths.append(2)
		if d3 > 2:
			d3 = 3/8
			x = d3-3
			paths.append(3)
		else:
			d3 = 0+d3
			d3 = n7/1
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		d3 = n7**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))