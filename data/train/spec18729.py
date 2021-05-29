import numpy as np 

def function(x):

	v8 = x
	d3 = 3
	paths = []
	try:
		if x >= 0:
			d3 = 2/x
			v8 = 1/7
			paths.append(1)
		else:
			d3 = d3*5
			paths.append(2)
		if x < 8:
			x = 1*v8
			x = x/v8
			d3 = 9*d3
			paths.append(3)
		else:
			v8 = v8*d3
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		d3 = v8**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))