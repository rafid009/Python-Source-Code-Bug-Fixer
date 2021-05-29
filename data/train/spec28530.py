import numpy as np 

def function(x):

	a0 = 0
	d3 = x
	paths = []
	try:
		if x > 7:
			a0 = x*9
			a0 = 7/d3
			a0 = a0*2
			paths.append(1)
		else:
			d3 = x-d3
			paths.append(2)
		if a0 < 7:
			d3 = 4+x
			paths.append(3)
		else:
			a0 = a0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))