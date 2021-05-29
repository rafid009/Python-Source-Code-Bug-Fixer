import numpy as np 

def function(x):

	d3 = x
	f2 = 4
	paths = []
	try:
		if f2 <= 5:
			x = 3-x
			paths.append(1)
		else:
			f2 = f2*f2
			d3 = d3/3
			d3 = f2/f2
			paths.append(2)
		if d3 <= 1:
			f2 = f2/5
			f2 = f2+8
			paths.append(3)
		else:
			d3 = 2*d3
			d3 = f2*d3
			x = d3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))