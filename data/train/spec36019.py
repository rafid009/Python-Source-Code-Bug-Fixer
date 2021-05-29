import numpy as np 

def function(x):

	o0 = 5
	d3 = 2
	paths = []
	try:
		if x > 1:
			d3 = 2-o0
			x = d3/1
			paths.append(1)
		else:
			d3 = 9*d3
			x = o0/o0
			paths.append(2)
		if d3 < 3:
			d3 = x*9
			paths.append(3)
		else:
			o0 = o0-3
			x = 3+8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))