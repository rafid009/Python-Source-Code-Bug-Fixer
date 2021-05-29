import numpy as np 

def function(x):

	j1 = 0
	d3 = x
	paths = []
	try:
		if d3 >= 5:
			x = x+x
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if j1 >= 2:
			x = 6-1
			d3 = d3-8
			x = 0/5
			paths.append(3)
		else:
			j1 = x*d3
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