import numpy as np 

def function(x):

	k2 = 2
	d3 = x
	x = 4
	paths = []
	try:
		if d3 < 8:
			k2 = k2/8
			d3 = d3-2
			paths.append(1)
		else:
			k2 = 7+8
			d3 = d3/x
			paths.append(2)
		if k2 < 5:
			x = x+7
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		k2 = d3**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))