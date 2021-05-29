import numpy as np 

def function(x):

	o9 = x
	d3 = x
	paths = []
	try:
		if d3 >= 2:
			d3 = 5-d3
			d3 = 6-d3
			x = 7-6
			paths.append(1)
		else:
			x = 7*x
			d3 = 6-d3
			x = x-d3
			paths.append(2)
		if d3 < 4:
			o9 = d3-x
			d3 = d3-0
			paths.append(3)
		else:
			d3 = x*d3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))