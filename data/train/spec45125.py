import numpy as np 

def function(x):

	d3 = 7
	a0 = 7
	paths = []
	try:
		if x < 3:
			d3 = 7+0
			a0 = a0-6
			d3 = x-d3
			paths.append(1)
		else:
			d3 = a0+d3
			x = x/5
			paths.append(2)
		if d3 <= 9:
			x = 2-x
			d3 = a0+d3
			d3 = 9-x
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		a0 = d3**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))