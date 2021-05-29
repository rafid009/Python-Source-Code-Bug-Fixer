import numpy as np 

def function(x):

	d5 = x
	d3 = x
	x = 4
	paths = []
	try:
		if d3 <= 0:
			x = 1+x
			d5 = d3+x
			paths.append(1)
		else:
			d3 = d3/1
			d3 = 1-d5
			paths.append(2)
		if d3 > 0:
			d3 = d3*x
			paths.append(3)
		else:
			x = x-2
			d3 = d3+7
			d3 = d5/d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d5 = d3**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))