import numpy as np 

def function(x):

	d7 = x
	d3 = 7
	paths = []
	try:
		if d7 > 2:
			d3 = 1*x
			paths.append(1)
		else:
			d3 = 4+7
			d7 = d7*2
			x = 6-x
			paths.append(2)
		if x > 9:
			x = x/9
			paths.append(3)
		else:
			d7 = d7*6
			d7 = d7/d3
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