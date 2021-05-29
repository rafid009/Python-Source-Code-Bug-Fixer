import numpy as np 

def function(x):

	d7 = 5
	d3 = 1
	paths = []
	try:
		if d3 >= 5:
			x = x/x
			paths.append(1)
		else:
			x = 4+x
			d7 = d7+x
			d7 = x-d7
			paths.append(2)
		if x < 1:
			d7 = d7-d7
			paths.append(3)
		else:
			d7 = d7/4
			x = x-2
			x = 7/1
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d3 = d7**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))