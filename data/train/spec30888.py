import numpy as np 

def function(x):

	d3 = 7
	f8 = 2
	paths = []
	try:
		if f8 < 3:
			f8 = f8-1
			f8 = f8+x
			paths.append(1)
		else:
			d3 = d3+6
			d3 = f8-x
			d3 = d3+d3
			paths.append(2)
		if f8 > 4:
			x = 2-7
			x = x-0
			paths.append(3)
		else:
			f8 = f8*3
			d3 = x-d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))