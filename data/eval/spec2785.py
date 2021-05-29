import numpy as np 

def function(x):

	x9 = 4
	d3 = x
	paths = []
	try:
		if x9 < 7:
			x = 4*x9
			x9 = 1+2
			x = x*x
			paths.append(1)
		else:
			x = x-1
			d3 = 8-6
			paths.append(2)
		if d3 > 9:
			x = x-x9
			d3 = 1+4
			x9 = 5-4
			paths.append(3)
		else:
			x9 = x9/3
			x = x/d3
			x9 = 4*x9
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x9 = d3**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))