import numpy as np 

def function(x):

	o9 = x
	d3 = x
	x = x
	paths = []
	try:
		if o9 <= 1:
			d3 = 9-x
			d3 = d3/x
			o9 = 8/o9
			paths.append(1)
		else:
			x = d3/1
			paths.append(2)
		if o9 >= 6:
			o9 = o9*d3
			x = 1-5
			x = d3*0
			paths.append(3)
		else:
			o9 = o9-6
			x = o9+x
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