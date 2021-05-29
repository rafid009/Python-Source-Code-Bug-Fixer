import numpy as np 

def function(x):

	d8 = 3
	d3 = x
	paths = []
	try:
		if d3 >= 4:
			d3 = d3/d3
			paths.append(1)
		else:
			x = 2/9
			paths.append(2)
		if x >= 7:
			d8 = 3*2
			d8 = 2+d3
			d8 = d8/7
			paths.append(3)
		else:
			x = d8-x
			d8 = d8-d8
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d8 = d3**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))