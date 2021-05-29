import numpy as np 

def function(x):

	d3 = x
	a3 = 5
	paths = []
	try:
		if a3 <= 0:
			a3 = 6+a3
			paths.append(1)
		else:
			a3 = a3-a3
			paths.append(2)
		if d3 >= 9:
			x = x-4
			d3 = d3*9
			paths.append(3)
		else:
			a3 = a3*x
			a3 = a3-2
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		a3 = d3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))