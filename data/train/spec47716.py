import numpy as np 

def function(x):

	d3 = 1
	r8 = 5
	paths = []
	try:
		if x > 6:
			r8 = 6*r8
			paths.append(1)
		else:
			r8 = x-2
			paths.append(2)
		if x <= 1:
			x = 6-d3
			paths.append(3)
		else:
			x = x-6
			d3 = d3/r8
			x = x-1
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))