import numpy as np 

def function(x):

	d3 = 4
	a7 = 2
	paths = []
	try:
		if x > 4:
			a7 = a7-a7
			a7 = a7-a7
			paths.append(1)
		else:
			a7 = a7-d3
			d3 = a7+5
			paths.append(2)
		if a7 >= 1:
			d3 = d3*7
			x = 5+x
			x = d3-x
			paths.append(3)
		else:
			a7 = x-2
			a7 = a7-a7
			d3 = x+d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))